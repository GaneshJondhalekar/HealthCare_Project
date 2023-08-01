from rest_framework import serializers
from .models import Patient
class PatientRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField()
    class Meta:
        model=Patient
        fields=['name','email','password']

class PatientLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    
class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['name','email']
