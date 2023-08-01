# permissions.py
from rest_framework import permissions

class IsPatientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print('Permissions hiiiiiiii')
        #print(request.user,request.user.is_patient())
        return request.user.is_authenticated and request.user.is_patient()
        
