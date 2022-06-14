
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/articles/', include('articles.urls')),
    # dj-rest-auth
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
]
