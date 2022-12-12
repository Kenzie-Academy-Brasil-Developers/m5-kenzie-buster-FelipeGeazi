from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from movies.models import *
from movies.serializers import *
from django.shortcuts import get_object_or_404
from movies.permissions import *
from rest_framework.pagination import PageNumberPagination


# Create your views here.


class MovieView(APIView,PageNumberPagination):

    """ authentication_classes = [JWTAuthentication] já configurado no setting"""
    permission_classes = [IsMoviePermission]  
    page_size = 2

    def get(self, request: Request):

        

        movies = Movie.objects.all()
        pages = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(pages, many= True)

        return self.get_paginated_response(serializer.data)

    def post (self, request: Request) -> Response:
        request.auth

        serializer = MovieSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    

class MovieDetailView(APIView):

    permission_classes = [IsMoviePermission] 
     

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id = movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT) 


class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request: Request, movie_id: int) -> Response:

        movie_obj = get_object_or_404(Movie, pk = movie_id)

        """ self.check_object_permissions(request, movie_obj) """
       
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie_obj, user = request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
        





