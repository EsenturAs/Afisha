from rest_framework import serializers
from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = "id name movies_count".split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = "__all__"


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewsForMovie(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = 'id title average_rating reviews'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False)

    def validate_name(self, name):
        if models.Director.objects.filter(name__exact=name):
            raise serializers.ValidationError("Director with this name already exists")
        if str(name).isnumeric():
            raise serializers.ValidationError("Director name mustn't be numeric")
        else:
            print(name)
            return name


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    description = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(required=False)

    def validate_title(self, title):
        if models.Movie.objects.filter(title__exact=title):
            raise serializers.ValidationError("Movie with this title already exists")
        if str(title).isnumeric():
            raise serializers.ValidationError("Movie title mustn't be numeric")
        else:
            return title

    def validate_director_id(self, director_id):
        try:
            models.Director.objects.get(id=director_id)
        except:
            raise serializers.ValidationError("This director does not exist")
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    movie_id = serializers.IntegerField(required=True)
    stars = serializers.IntegerField(max_value=5, min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            models.Movie.objects.get(id=movie_id)
        except:
            raise serializers.ValidationError("This movie does not exist")
        return movie_id
