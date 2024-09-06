from django.urls import path
from .views import get_users, create_user, user_detail, ping_pong

urlpatterns = [
    path('users/', get_users, name = 'get_users'),
    path('users/create/', create_user, name = 'create _user'),
    path('users/<int:pk>/', user_detail, name = 'user_detail'),
    path('ping/', ping_pong, name = 'ping_pong')
]