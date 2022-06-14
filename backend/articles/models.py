from django.db import models
from django.conf import settings

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=10)

# 게시판 글쓰기
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 글 좋아요하기 -> 찜 개수 글 화면에 알려주고, 개인 프로필에도 어떤것들 좋아요해뒀는지 나오게해줄때 사용
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # 어디 커뮤니티에 글 썼는지!
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='article_find')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
