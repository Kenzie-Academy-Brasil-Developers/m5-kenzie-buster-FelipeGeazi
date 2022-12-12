from django.urls import path
from users.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", RegisterView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("users/<int:user_id>/", UserDetailsView.as_view())
    
]
