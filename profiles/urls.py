from django.urls import path
from .views import (
    my_profile_view,
    profile_detail
)
app_name = 'profiles'

urlpatterns = [
    path('my/', my_profile_view, name='my_profile'),
    path('<pk>/', profile_detail, name='profile_detail'),
]