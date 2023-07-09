from rest_framework import serializers
from .models import Patient
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['email','first_name', 'last_name','password','DOB']


class PatientLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    def generate_jwt_token(self, patient):
        payload = api_settings.JWT_PAYLOAD_HANDLER(patient)
        token = api_settings.JWT_ENCODE_HANDLER(payload)
        return token