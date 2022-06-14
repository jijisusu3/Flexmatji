from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
    followers = UserSerializer(read_only=True, many=True)
    followings = UserSerializer(read_only=True, many=True)

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'overview','vote_average')
    like_movie = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'


class MyMovieSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'overview','vote_average')
    like_movie = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

