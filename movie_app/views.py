from django.shortcuts import render
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms import model_to_dict
from . import models, serializers


@api_view(http_method_names=['GET'])
def director_list_view(request):
    directors = models.Director.objects.all()
    # list_ = []
    # for director in directors:
    #     list_.append(model_to_dict(director))
    serializer = serializers.DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def movie_list_view(request):
    movies = models.Movie.objects.all()
    serializer = serializers.MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def review_list_view(request):
    reviews = models.Review.objects.all()
    serializer = serializers.ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_view(request, id):
    director = models.Director.objects.get(id=id)
    data = serializers.DirectorDetailSerializer(director).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, id):
    movie = models.Movie.objects.get(id=id)
    data = serializers.MovieDetailSerializer(movie).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, id):
    review = models.Review.objects.get(id=id)
    data = serializers.ReviewSerializer(review).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_for_movie_list_view(request):
    movies = models.Movie.objects.all()
    serializer = serializers.ReviewsForMovie(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
