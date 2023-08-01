from django.shortcuts import render
from .models import Patient
from .serializers import PatientRegistrationSerializer,PatientLoginSerializer,DemoSerializer
from rest_framework import views,viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPatientUser

# Create your views here.

class PatientRegistrationViewset(viewsets.ModelViewSet):
    serializer_class=PatientRegistrationSerializer
    queryset=Patient.objects.all()

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            patient=serializer.save()
            patient.set_password(serializer.validated_data['password'])
            patient.user_type='patient'
            patient.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#@method_decorator(login_required,name='dispatch')
class demo(views.APIView):
    serializer_class=DemoSerializer
    permission_classes=[IsPatientUser]
    def get(self,request):
        p=Patient.objects.all()
        serializer=self.serializer_class(p,many=True)
        print(request.user)
        return Response(serializer.data)

    
        
