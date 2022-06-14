from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, MovieComment, Genre, Actor

User = get_user_model()



class MovieCommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = MovieComment
        fields = ('pk', 'user', 'content', 'movie',)
        read_only_fields = ('movie',)




class MovieSerializer(serializers.ModelSerializer):

    movie_comments = MovieCommentSerializer(read_only=True, many=True)
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('pk', 'name')
    genres = GenreSerializer(read_only=True, many=True)


    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name')
    
    actors = ActorSerializer(read_only=True, many=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    like_users = UserSerializer(read_only=True, many=True)


    class Meta:
        model = Movie
        fields = '__all__'



class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
