from rest_framework import serializers
from users.models import *
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(write_only= True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate= serializers.DateField(allow_null= True, default = "")
    is_employee = serializers.BooleanField(allow_null= True, default=False)
    is_superuser = serializers.BooleanField(read_only= True)



    def create(self, validated_data : dict):
        employee=  validated_data["is_employee"]
        
        if employee:
           
            user =  User.objects.create_superuser(**validated_data)
            
        else:
            
             user = User.objects.create_user(**validated_data)

        return user


    def validate_email(self, email: str) -> str:
        email_already_exists = User.objects.filter(email=email).exists()

        if email_already_exists:
            raise serializers.ValidationError(detail="email already registered.")

        return email

    def validate_username(self, username: str) -> str:
        username_already_exists = User.objects.filter(username=username).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already taken.")

        return username 

""" class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)
        is_supeuser = serializers.BooleanField(read_only=True)    
     """


   