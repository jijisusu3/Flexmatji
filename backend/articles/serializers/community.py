from rest_framework import serializers
from ..models import Community, Article

class CommunitySerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('id','title', 'content')

    article_find = ArticleSerializer(many=True)

    class Meta:
        model = Community
        fields = '__all__'