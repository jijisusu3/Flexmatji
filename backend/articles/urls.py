from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # articles
    path('', views.article_list_or_create), # 커뮤니티 전체 메인 페이지
    path('<int:article_pk>/detail/', views.article_detail_or_update_or_delete),
    path('<community_pk>/', views.community_detail),
 
    path('<int:article_pk>/like/', views.like_article),
    # comments
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]