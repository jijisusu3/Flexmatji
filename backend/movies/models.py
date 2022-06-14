from distutils.text_file import TextFile
from django.db import models
from django.conf import settings



class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Actor(models.Model):    
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    youtube_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='moviegenre')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie', blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    keywords = models.ManyToManyField(Keyword, related_name='moviekeywords')
    def __str__(self):
        return self.title

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comments')
    # 별점만 줄 수 있게
    content = models.TextField(max_length=300, null=True)
    # 별점주기
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

class TodayRecommend(models.Model):
    date = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    overview = models.TextField()

    def __str__(self):
        return self.date

class Enmovie(models.Model):
    overview = models.TextField(null=True)

    def __str__(self):
        return self.overview