from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser,PermissionsMixin,Permission,Group


class PatientManager(BaseUserManager):

    #use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.user_type='admin'
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)




class Patient(AbstractBaseUser,PermissionsMixin):
    #user_permissions = models.ManyToManyField(Permission,verbose_name=('user permissions'),blank=True,related_name='patient')

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    #is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,related_name='group_patients')
    user_permissions=models.ForeignKey(Permission,on_delete=models.CASCADE,null=True,related_name='permissions_patients')
    user_type=models.CharField(default='patient',max_length=10)
    objects = PatientManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    
    def is_patient(self):
        return self.user_type == 'patient'

    def is_pharma(self):
        return self.user_type == 'pharma'