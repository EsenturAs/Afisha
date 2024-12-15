from django.shortcuts import render, get_object_or_404
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms import model_to_dict
from . import models, serializers


@api_view(http_method_names=['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        # list_ = []
        # for director in directors:
        #     list_.append(model_to_dict(director))
        serializer = serializers.DirectorSerializer(instance=directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        name = request.data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED, data=serializers.DirectorSerializer(director).data)


@api_view(http_method_names=['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = models.Movie.objects.create(title=title,
                                            description=description,
                                            duration=duration,
                                            director_id=director_id)
        return Response(status=status.HTTP_201_CREATED, data=serializers.MovieSerializer(movie).data)


@api_view(http_method_names=['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(instance=reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = models.Review.objects.create(text=text,
                                              movie_id=movie_id,
                                              stars=stars)
        return Response(status=status.HTTP_201_CREATED, data=serializers.ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    director = models.Director.objects.get(id=id)
    director = get_object_or_404(models.Director, id=id)
    if request.method == 'GET':
        data = serializers.DirectorDetailSerializer(director).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        director.name = request.data.get('name')
        director.save()
        return Response(status=status.HTTP_204_NO_CONTENT, data=serializers.DirectorDetailSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    movie = models.Movie.objects.get(id=id)
    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(movie).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id', 'none')
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT, data=serializers.MovieDetailSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    review = models.Review.objects.get(id=id)
    if request.method == 'GET':
        data = serializers.ReviewSerializer(review).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(status=status.HTTP_204_NO_CONTENT, data=serializers.ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def reviews_for_movie_list_view(request):
    movies = models.Movie.objects.all()
    serializer = serializers.ReviewsForMovie(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
