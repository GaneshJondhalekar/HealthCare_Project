from rest_framework import serializers
from .models import Pharma
class PharmaRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField()
    class Meta:
        model=Pharma
        fields=['name','email','password']

class PharmaLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

class demoserializer(serializers.ModelSerializer):
    class Meta:
        model=Pharma
        fields='__all__'
    

