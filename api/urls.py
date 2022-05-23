from django.urls import path

from api.profile import profile

urlpatterns = [
    path("profile", profile.index),
    path("login", profile.login),
    path("me", profile.me),
]
