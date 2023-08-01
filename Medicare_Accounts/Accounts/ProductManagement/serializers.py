from .models import Product
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

