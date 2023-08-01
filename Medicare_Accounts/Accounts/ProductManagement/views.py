from django.shortcuts import render
from rest_framework import views,viewsets,status,generics
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import pharma_login_required
from Patients.permissions import IsPatientUser
from .models import Product

from .serializers import ProductAddSerializer,ProductListSerializer
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
   

  