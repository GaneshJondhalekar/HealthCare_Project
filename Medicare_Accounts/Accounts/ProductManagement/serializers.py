from .models import Product,CartItems,Cart,Order,OrderItem
from rest_framework import serializers

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude=['pharmacy']
        #fields='__all__'

class ProductListSerializer(serializers.HyperlinkedModelSerializer):

    #url=serializers.HyperlinkedRelatedField(view_name='product-details', lookup_field='id',read_only=True )
    class Meta:
        model = Product
        fields = ['url','id', 'name', 'price', 'description', 'image']
        extra_kwargs = {
            'url': {'view_name': 'product_details', 'lookup_field': 'id'}
        }


class AddProductToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItems
        fields=['product','quantity']
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','price']


class ProductDetailsSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=CartItems
        fields=['product','quantity']

class CartItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=False)
    total_price=serializers.SerializerMethodField(method_name='Total_price')
    class Meta:
        model=CartItems
        fields=['id','cart','product','quantity','total_price']
    
    def Total_price(self,cartitem:CartItems):
        return cartitem.quantity*cartitem.product.price

class MyCartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True)
    final_total=serializers.SerializerMethodField(method_name='Final_total')
    class Meta:
        model=Cart
        fields=['user','items','final_total']

    def Final_total(self,cart:Cart):
        items=cart.items.all()
        return sum([item.quantity*item.product.price for item in items])

class PlaceOrderSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField(required=True)


class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=False)
    class Meta:
        model=OrderItem
        fields=['product','quantity','subtotal']


class MyOrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['user','items','total_price','payment_status','status']