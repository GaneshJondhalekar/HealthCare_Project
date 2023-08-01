from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Permission,Group

# Create your models here.
class PharmaManager(BaseUserManager):

    #use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

class Pharma(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    #is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,related_name='group_pharma')
    user_permissions=models.ForeignKey(Permission,on_delete=models.CASCADE,null=True,related_name='permissions_pharma')
    user_type=models.CharField(default='pharma',max_length=10)
    
    objects = PharmaManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def is_patient(self):
        return self.user_type == 'patient'

    def is_pharma(self):
        return self.user_type == 'pharma'
    