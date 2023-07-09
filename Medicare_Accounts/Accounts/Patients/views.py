from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PatientSerializer,PatientLoginSerializer
from .models import Patient
from rest_framework_jwt.views import ObtainJSONWebToken
# Create your views here.

class PatientViewSet(ModelViewSet):
    serializer_class=PatientSerializer
    queryset=Patient.objects.all()

class PatientLoginView(ObtainJSONWebToken):
    serializer_class=PatientLoginSerializer