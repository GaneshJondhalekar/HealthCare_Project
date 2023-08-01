from django.shortcuts import render
from rest_framework import views,viewsets,status
from .serializers import PharmaRegistrationSerializer,PharmaLoginSerializer,demoserializer
from .models import Pharma
from rest_framework.response import Response
from django.contrib.auth import login,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .backends import CustomPharmaBackend 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPharmaUser
# Create your views here.

class PharmaRegistrationViewset(viewsets.ModelViewSet):
    serializer_class=PharmaRegistrationSerializer
    queryset=Pharma.objects.all()

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pharma=serializer.save()
            pharma.set_password(serializer.validated_data['password'])
            pharma.user_type='pharma'
            pharma.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    

class PharmaLoginView(views.APIView):
    serializer_class=PharmaLoginSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            print(email,password)
            backend=CustomPharmaBackend()
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                refresh=RefreshToken.for_user(user)
                return Response({'Success':'Login Successful','user_type':str(user.user_type),'refresh':str(refresh),'access_token':str(refresh.access_token)})
            return Response({'msg':'Usrname or password invalid'})
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST) 

#@method_decorator(login_required,name='dispatch')
class Demo(views.APIView):
    serializer_class=demoserializer
    permission_classes=[IsPharmaUser]
    def get(self, request):
        pharma_objects = Pharma.objects.all()
        print(request.user)
        serializer = self.serializer_class(pharma_objects, many=True)
        return Response(serializer.data)
   