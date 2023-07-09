from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.

class Patient(AbstractBaseUser):
    email=models.EmailField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    DOB=models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email