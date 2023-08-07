from django.shortcuts import render
from rest_framework import views,viewsets,status,generics
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import pharma_login_required
from Patients.permissions import IsPatientUser
from .models import Product,Cart,CartItems,Order,OrderItem
from rest_framework.exceptions import NotFound 
from django.db import transaction

from .serializers import *
# Create your views here.

#@method_decorator(login_required,name='dispatch')  
class ProductAddView(views.APIView):
    serializer_class=ProductAddSerializer
    permission_classes=[IsPatientUser]
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        print(f'....{request.user}...{request.user.is_authenticated}')
        if serializer.is_valid(raise_exception=True):
            product=serializer.save()
            product.pharmacy=request.user.id
            product.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
   

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'

class AddProductToCartView(views.APIView):
    serializer_class=AddProductToCartSerializer
    permission_classes=[IsPatientUser]
    def post(self,request):
        
        cart,created=Cart.objects.get_or_create(user=request.user)
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cartitem=serializer.save(cart=cart)
            print('hi.....................')
           
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self,request,id):
        try:
            print('hi')
            cartitem=CartItems.objects.get(pk=id)
            serializer=ProductDetailsSerializer(cartitem)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def patch(self,request,id):
        try:
            print('hi',request.data)
            cartitem=CartItems.objects.get(pk=id)
            cartitem.quantity=request.data.get('quantity')
            #cartitem.product.price=request.data.get('price')
            cartitem.save()
            serializer=ProductDetailsSerializer(cartitem)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


   
class MyCartView(views.APIView):
    serializer_class=MyCartSerializer
    permission_classes=[IsPatientUser]

    def get(self,request):
        cart=Cart.objects.filter(user=request.user)
        #cartitems=CartItems.objects.filter(cart=cart)
        serializer=self.serializer_class(cart,many=True)
        return Response(serializer.data)


class PlaceOrderView(views.APIView):
    serializer_class=PlaceOrderSerializer
    permission_classes=[IsPatientUser]

    def post(self,request):
        #cart_id=request.data.get('cart_id')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)  # Raise validation error if data is invalid
        cart_id = serializer.validated_data['cart_id']
        try:
            with transaction.atomic():#Wrap the entire order creation process in a database transaction using the transaction.atomic(). 
                #This ensures that if any part of the process fails, the changes are rolled back, maintaining data integrity.
                cart=Cart.objects.get(id=cart_id)
                cartitems=CartItems.objects.filter(cart=cart)
                order=Order.objects.create(user=request.user, status='PENDING',total_price=0.0)
                orderitems=[OrderItem(order=order,quantity=cartitem.quantity,product=cartitem.product,subtotal=cartitem.product.price * cartitem.quantity) for cartitem in cartitems]
                OrderItem.objects.bulk_create(orderitems)
                total=sum(orderitem.subtotal for orderitem in orderitems)
                order.total_price=total
                order.payment_status='PENDING'
                order.save()
                cart.delete()
        except Cart.DoesNotExist:
            raise NotFound("Cart not found")
        return Response({'msg':"order placed"})
       
class MyOrdersView(viewsets.ModelViewSet):
    serializer_class=MyOrderSerializer
    permission_classes=[IsPatientUser]
    def get_queryset(self):
        orders=Order.objects.filter(user=self.request.user)
        return orders
    

  