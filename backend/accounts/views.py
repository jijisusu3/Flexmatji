from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.http import require_POST

from flixmatji.settings import SECRET_KEY
from .serializers import ProfileSerializer, MyMovieSerializer

# Create your views here.

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def mymovie(request, username):
    user = get_object_or_404(User, username=username)
    serializer = MyMovieSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
        # if me in you.followers.all():
            # 언팔로우
            you.followers.remove(me)
            serializer = ProfileSerializer(you)
            return Response(serializer.data)
        else:
            # 팔로우
            you.followers.add(me)
            serializer = ProfileSerializer(you)
            return Response(serializer.data)

    return JsonResponse({'message':'팔로우 or 언팔로우 실패'})


# import requests
# # Create your views here.
# from django.contrib.auth import login as auth_login
# User = get_user_model()
# import json
# import jwt
# from rest_framework.authtoken.models import Token
# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def kakaologin(request):
#     kakao_access_code = request.GET.get('code', None)
#     print(type(kakao_access_code))
#     url = 'https://kauth.kakao.com/oauth/token'
#     headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
#     body = {'grant_type':'authorization_code',
#         'client_id':'2bdbfc007fb0f44e741f6cdcda9cd34b',
#         'redirect_uri':'http://127.0.0.1:8000/api/v1/accounts/kakaologin/oauth/',
#         'code': kakao_access_code
#     }
#     token_kakao_response = requests.post(url, headers=headers, data=body)
#     access_token = json.loads(token_kakao_response.text).get('access_token')
#     url = 'https://kapi.kakao.com/v2/user/me'
#     headers = {
#         'Authorization':f'Bearer {access_token}',
#         'Content-type':'application/x-www-form-urlencoded; charset=utf-8'
#     }
#     kakao_response = requests.get(url, headers=headers)
#     kakao_response = json.loads(kakao_response.text)
#     print(kakao_response)
#     if User.objects.filter(username=kakao_response['id']).exists():
#         user = User.objects.get(username=kakao_response['id'])        
#         token = Token.objects.create(user=user)
#         data = {
#             "username": user.username,
#             "key": token,
#             "id":user.id
#         }
#         print(data)
#         return JsonResponse(data)

#     User(
#         id = kakao_response['id'],
#         username = kakao_response['properties']['nickname'],
#     ).save()
#     user = User.objects.get(id=kakao_response['id'])
#     token = Token.objects.create(user=user)
#     data = {
#         "username": user.username,
#         "key": token,
#         "id":user.id
#     }
#     print(data)
#     return Response(data)
    