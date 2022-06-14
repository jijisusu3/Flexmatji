from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from .models import Genre, Movie, Actor, MovieComment, Keyword, TodayRecommend, Enmovie

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer, MovieCommentSerializer, MovieListSerializer




@api_view(['GET'])
def movie_detail(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        
        comments = movie.movie_comments.all()
        serializer = MovieCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = MovieCommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.movie_comments.all()
                serializer = MovieCommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.movie_comments.all()
            serializer = MovieCommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()



@api_view(['GET'])
def home(request):
    # 홈에 보여줄 영화들 popularity 170보다 큰 것들 중 랜덤으로 10개씩 populer에서 뽑아줌
    movies = Movie.objects.filter(popularity__gt=170).order_by('?')[0:12]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    # 영화 목록 추천해주기! 


API_KEY = 'f41a632573e0b9ac1edf1ef69233891d'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'


# def genre_data(request):
#     response = requests.get(
#         GENRE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',            
#         }
#     ).json()

#     for genre in response.get('genres'):
#         Genre.objects.create(
#             id=genre.get('id'),
#             name=genre.get('name')
#         )
#     return JsonResponse(response)

# youtube 동영상 key
def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

# movie에 출연한 배우 정보
def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'en-US',
        }
    ).json()
    
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
        movie.actors.add(actor_id)
        if movie.actors.count() == 5:
            break


def keyword_data(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/keywords',
        params={
            'api_key': API_KEY,
            'language': 'en-US',
        }
    ).json()
    for keyword in response.get('keywords'):
        keyword_id = keyword.get('id')
        if not Keyword.objects.filter(pk=keyword_id).exists():
            keyword = Keyword.objects.create(
                id=keyword.get('id'),
                name=keyword.get('name')
            )
        movie.keywords.add(keyword_id)


def movie_data(page=1):
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'en-US',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)
        
        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        keyword_data(movie)
        get_actors(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)


def tmdb_data(request):
    for i in range(400, 350, -1):
        movie_data(i)
    return HttpResponse('OK>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')




# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import ast
# import sys 
# sys.path.append("C:/Users/Jisu/final-project/flixmatji/pjt/pjt/final-pjt-back/")
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flixmatji.settings")
# import django
# django.setup()
# from movies.models import Movie
# import requests
# from movies.models import Movie, Genre, Actor, Keyword
# from django.shortcuts import get_object_or_404
# import json
# import csv

# def recommendedCsv(request):
#     movies = Movie.objects.all()
#     col = {'movie_id':[], 'title':[], 'tags':[]}
#     movie_tags = pd.DataFrame(col)
#     for movie in movies:
#         tag = movie.overview
#         tag += ' '
#         keywords = movie.keywords.all()
#         for k in keywords:
#             tag += k.name
#             tag += ' '

#         genres = movie.genres.all()
#         for g in genres:
#             tag += g.name
#             tag += ' '
        
#         data = {'movie_id': int(movie.id), 'title': movie.title, 'tags':tag} 
#         movie_tags = movie_tags.append(data, ignore_index=True)
    
#     movie_tags.to_csv('movie_tags.csv', encoding='utf-8')
#     return HttpResponse({'message':'열받아'})


    # with open('movie_tags.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldsnames=)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from movies.models import Movie, Genre, Actor
import requests
from django.shortcuts import get_object_or_404


# def recommend(movie_title):
#     movie_tags= pd.read_csv('./movies/movie_tags.csv', encoding='UTF-8')
#     lv = TfidfVectorizer(max_features=5000, stop_words='english')
#     vector = lv.fit_transform(movie_tags['tags']).toarray()
#     similarity = cosine_similarity(vector)
#     movie_title = movie_title.strip()
#     result = []
#     if not movie_tags[movie_tags['title'] == movie_title].empty:
#         index = movie_tags[movie_tags['title'] == movie_title].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#         for i in distances[0:10]:
#             if movie_tags.iloc[i[0]].title:
#                 result.append(movie_tags.iloc[i[0]].title)
#     return result

def recommend(movie_id_list):
 # 리스트로 들어가도 잘 됨!!!!!
    movie_tags= pd.read_csv('./movies/movie_tags.csv', encoding='UTF-8')
    lv = TfidfVectorizer(max_features=5000, stop_words='english')
    vector = lv.fit_transform(movie_tags['tags']).toarray()
    similarity = cosine_similarity(vector)
    result = []
    for movie_id in movie_id_list:
        if not movie_tags[movie_tags['movie_id'] == movie_id].empty:
            index = movie_tags[movie_tags['movie_id'] == movie_id].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            for i in distances[1:10]:
                result.append(movie_tags.iloc[i[0]].movie_id)
        else: continue
    return result



# def today_recommend(movie_id_list):
#  # 리스트로 들어가도 잘 됨!!!!!
#     movie_tags= pd.read_csv('./movies/movie_tags.csv', encoding='UTF-8')
#     date_overview = pd.read_csv('./movies/dateoverview.csv', encoding='UTF-8')

#     lv = TfidfVectorizer(max_features=5000, stop_words='english')

#     vector = lv.fit_transform(date_overview['overview']).toarray()
#     similarity = cosine_similarity(vector)
#     result = []
#     # index = movie_tags[movie_tags['movie_id'] == movie_id].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     for i in distances[1:5]:
#         result.append(movie_tags.iloc[i[0]].movie_id)


#     return result


# from datetime import datetime
# def today_recommend(request):
#     # today = datetime.today().strftime("%m-%d")
#     # date = get_object_or_404(TodayRecommend, date=today)
#     # result = today_recommend(date.pk)
#     movies = get_object_or_404(Movie, id=5)
#     print(type(movies))


#     return


    
import random
@api_view(['GET'])
def movie_recommend(request):
    user_like_movie = []
    movies = Movie.objects.filter(like_users=request.user.id)
    for movie in movies:
        user_like_movie.append(movie.id)
    movie_list = recommend(user_like_movie)
    if movie_list:
        movies = []
        for movie_id in movie_list:
            a = Movie.objects.filter(pk=int(movie_id))
            if a:
                movies.append(Movie.objects.filter(pk=movie_id)[0])
        if not movies:
            return Response({'message': '당신이 좋아하는 영화에 대한 정보가 부족합니다.'})
        sample_list = random.sample(movies, 4)
        serializer = MovieListSerializer(sample_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




from datetime import datetime
import math 
import re
from collections import Counter


def get_cosign(id, movie_overview, date_overview):
    intersection = set(movie_overview.keys())&set(date_overview.keys())
    numerator = sum([movie_overview[x]*date_overview[x] for x in intersection])
    sum1 = sum([movie_overview[x]**2 for x in list(movie_overview.keys())])
    sum2 = sum([date_overview[x]**2 for x in list(date_overview.keys())])
    denominator = math.sqrt(sum1)*math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return [id, float(numerator)/denominator]



@api_view(['GET'])
def index(request):
    WORD =re.compile(r"\w+")
    today = datetime.today().strftime("%m-%d")
    date = get_object_or_404(TodayRecommend, date="12-25")
    movies = Enmovie.objects.all()[1:1500]
    if date:
        result = []
        word1 = WORD.findall(date.overview)
        date_overview = Counter(word1)
        for movie in movies:
            word2 = WORD.findall(movie.overview)
            movie_overview = Counter(word2)
            temp_result = get_cosign(movie.id, movie_overview, date_overview)
            result.append(temp_result)
        result.sort(key=lambda x:x[1])
    print(result)
    if result:
        X = []
        for movie in result[1470:1500]:
            a = Movie.objects.filter(pk=int(movie[0]))
            if a:
                X.append(Movie.objects.filter(pk=int(movie[0]))[0])
        X2 = reversed(X)
        serializer = MovieListSerializer(X2, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



        #     if get_object_or_404(Movie, pk=movie[0]):
        #         a = get_object_or_404(Movie, pk=movie[0])
        #         X.append(a)
        # print(X)
        # serializer = MovieListSerializer(X, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
    #     for movie_id in movie_list:
    #         a = Movie.objects.filter(pk=int(movie_id))
    #         if a:
    #             movies.append(Movie.objects.filter(pk=movie_id)[0])
    #     if not movies:
    #         return Response({'message': '당신이 좋아하는 영화에 대한 정보가 부족합니다.'})
    #     sample_list = random.sample(movies, 4)
    #     serializer = MovieListSerializer(sample_list, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response({'message':'메롱'})