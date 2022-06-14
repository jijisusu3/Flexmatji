from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('mymovie/<username>/', views.mymovie),
    # path('kakaologin/oauth/', views.kakaologin),
]
# http://127.0.0.1:8000/api/v1/accounts/kakaologin/oauth/