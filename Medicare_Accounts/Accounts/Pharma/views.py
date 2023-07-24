from django.shortcuts import render
from rest_framework import views,viewsets,status
from .serializers import PhrmaRegistrationSerializer,PharmaLoginSerializer
from .models import Pharma
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class PharmaRegistrationViewset(viewsets.ModelViewSet):
    serializer_class=PhrmaRegistrationSerializer
    queryset=Pharma.objects.all()

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pharma=serializer.save()
            pharma.set_password(serializer.validated_data['password'])
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
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                refresh=RefreshToken.for_user(user)
                return Response({'Success':'Login Successful','refresh':str(refresh),'access_token':str(refresh.access_token)})
            return Response({'msg':'Usrname or password invalid'})
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST) 
