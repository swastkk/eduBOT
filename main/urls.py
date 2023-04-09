from django.urls import path, re_path
from django.urls.conf import include
from .views import home, profile

urlpatterns= [
    path('', home, name='home'),
    path('profile', profile, name="profile"),
]
