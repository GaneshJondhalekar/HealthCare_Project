from django.contrib.auth.backends import ModelBackend
from .models import Patient

class CustomPatientBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        print("hi...................patin..")
        try:
            user = Patient.objects.get(email=email)

            if user.check_password(password):
                return user
        except Patient.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Patient.objects.get(pk=user_id)
        except Patient.DoesNotExist:
            return None