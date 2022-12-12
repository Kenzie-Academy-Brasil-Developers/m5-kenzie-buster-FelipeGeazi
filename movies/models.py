from django.db import models
from users.models import *

# Create your models here.

class Rating(models.Choices):
    PG = "PG"
    PG_13 = "PG-13"
    NC_17 = "NC-17"
    R = "R"
    DEFAULT = "G"




class Movie(models.Model):
   title = models.CharField(max_length=127) 
   duration = models.CharField(max_length=10, null= True)
   rating = models.CharField(max_length=20, default= Rating.DEFAULT)
   synopsis = models.TextField(null= True)
   user = models.ForeignKey("users.User", on_delete= models.CASCADE, related_name= "movies")
   """ user = models.ManyToManyField(User, through="movies.MovieOrder", related_name= "movies") """


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey("users.User", on_delete= models.CASCADE, related_name = "user_movies")
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE, related_name= "movie_users")