from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # path('', views.tmdb_data),
    # 영화 메인 페이지
    path('', views.index),
    # 영화 detail -> movie_title 가지고 서버에 요청 보내서 detail 가져오기 detail
    # 영화 detail 내에 영화 찜하기
    path('<int:movie_pk>/like/', views.like_movie),
    # detail 내에 영화 코멘트(후기) 달기
    path('<int:movie_pk>/comments/', views.create_comment),
    # detail 내에 영화 코멘트(후기) delete, update
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('home/', views.home),
    path('recommend/', views.movie_recommend),
    path('<movie_title>/', views.movie_detail),
]
