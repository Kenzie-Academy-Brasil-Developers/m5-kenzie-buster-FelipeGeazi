
from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View
from movies.models import *
from users.models import *

class IsUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, user) -> bool:
       
        if request.user.is_authenticated and request.user.is_superuser or  user == request.user :
            return True   
                
                



""" class IsPermissionUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True    """
        

