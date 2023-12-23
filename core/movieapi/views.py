from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg

from .models import Movies, Review
from .serializers import MoviesSerializer, ReviewSerializer


class MoviesListApiView(APIView):
    def get(self, request):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesDetailApiView(APIView):
    def get_movie(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return None

    def get(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            serializer = MoviesSerializer(movie)
            return Response(serializer.data)
        return Response(
            {"status": "NOT FOUND", "details": f"Movie {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    def put(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            serializer = MoviesSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"status": "NOT FOUND", "details": f"Movie {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    def delete(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"status": "NOT FOUND", "details": f"Movie {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

class ReviewListApiView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailApiView(APIView):
    def get_review(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return None

    def get(self, request, pk):
        review = self.get_review(pk)
        if review:
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        return Response(
            {"status": "NOT FOUND", "details": f"Review {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def put(self, request, pk):
        review = self.get_review(pk)
        if review:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"status": "NOT FOUND", "details": f"Review {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def delete(self, request, pk):
        review = self.get_review(pk)
        if review:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"status": "NOT FOUND", "details": f"Review {pk} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
class MovieStatsApiView(APIView):
    def get(self, request):
        movie_stats = Movies.objects.annotate(average_score=Avg('review__score')).values('id', 'title', 'average_score')

        movie_stats = [
            {
                'movie_id': stat['id'],
                'title': stat['title'],
                'average_score': stat['average_score'] if stat['average_score'] else 0.0
            }
            for stat in movie_stats
        ]

        return Response(movie_stats)