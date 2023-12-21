from rest_framework import serializers
from .models import Movies, Review

class MoviesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movies
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'