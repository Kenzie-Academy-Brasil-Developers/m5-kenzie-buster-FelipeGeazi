from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View
from movies.models import *
from users.models import *

class IsMoviePermission(permissions.BasePermission):
     """ def has_object_permission(self, request, view, user: User) -> bool:
        return user.user == request.user """


     def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True   
       
 
      


    