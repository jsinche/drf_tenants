from django.urls import path
from users.api.api import UserAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_list'),
]