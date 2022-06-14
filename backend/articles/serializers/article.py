from rest_framework import serializers
from django.contrib.auth import get_user_model


from ..models import Article, Community
from .comment import CommentSerializer

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)

    
    class CommunitySerializer(serializers.ModelSerializer):

        class Meta:
            model = Community
            fields = '__all__'
    
    communinty_id = CommunitySerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = '__all__'