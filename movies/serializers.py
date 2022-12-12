from rest_framework import serializers
from movies.models import *
from users.models import *
import ipdb

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(max_length= 20, required = False)
    rating = serializers.ChoiceField(
        choices= Rating.choices,
        default= Rating.DEFAULT,
        required = False
    )
    synopsis = serializers.CharField(required = False)
    added_by = serializers.SerializerMethodField(read_only= True)


    def get_added_by(self, obj: User) -> str:
        added_by = obj.user.email

        return added_by


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    """ movie = serializers.SerializerMethodField() """
    """ user = serializers.SerializerMethodField() """


    def get_title (self, obj: Movie) -> str:
        
        title = obj.movie.title

        return title

    def get_buyed_by (self, obj: User) -> str:
        buyed_by = obj.user.email

        return buyed_by 



    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)    