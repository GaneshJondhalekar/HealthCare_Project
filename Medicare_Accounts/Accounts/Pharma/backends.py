from django.contrib.auth.backends import ModelBackend
from .models import Pharma

class CustomPharmaBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        print("hi.....................")
        try:
            user = Pharma.objects.get(email=email)

            if user.check_password(password):
                return user
        except Pharma.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Pharma.objects.get(pk=user_id)
        except Pharma.DoesNotExist:
            return None