from rest_framework import serializers
from .models import Pharma
class PhrmaRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField()
    class Meta:
        model=Pharma
        fields=['name','email','password']

class PharmaLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    

