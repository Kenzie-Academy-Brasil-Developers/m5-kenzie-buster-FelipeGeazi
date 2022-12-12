from rest_framework.views import APIView, Request, Response, status
from users.serializers import *
from users.models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from users.permissions import *
# Create your views here.

class RegisterView(APIView):

    def get(self, request: Request) -> Response:

        users = User.objects.all() 
        serializers = UserSerializer(users, many = True)  

        return Response(serializers.data)
   
    def post(self, request: Request) -> Response:
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

    

        return Response(serializers.data, status.HTTP_201_CREATED)

""" class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializers= TokenObtainPairSerializer(data=request.data)
        serializers.is_valid(raise_exception= True)

        return Response(serializers.validated_data) """

class UserDetailsView(APIView):

        permission_classes = [IsAuthenticated ,IsUserPermission] 

        def get(self,request: Request,  user_id: int) -> Response:
            user_obj = get_object_or_404(User, id = user_id)

            self.check_object_permissions(request, user_obj)
        
            serializer = UserSerializer(user_obj)
            return Response(serializer.data)            