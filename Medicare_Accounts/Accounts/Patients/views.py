from django.shortcuts import render
from .models import Patient
from .serializers import PatientRegistrationSerializer,PatientLoginSerializer
from rest_framework import views,viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class PatientRegistrationViewset(viewsets.ModelViewSet):
    serializer_class=PatientRegistrationSerializer
    queryset=Patient.objects.all()

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            patient=serializer.save()
            patient.set_password(serializer.validated_data['password'])
            patient.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PatientLoginView(views.APIView):
    serializer_class=PatientLoginSerializer
    
    def post(self,request):

        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user=authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                refresh=RefreshToken.for_user(user)
                return Response({'Success':'Login Successful','refresh':str(refresh),'access_token':str(refresh.access_token)})
            else:
                 return Response({'Failed':'Username or password incorrect'})
        return Response(serializer.errors)

    
        
