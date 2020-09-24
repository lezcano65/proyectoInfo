from django.urls import path
from .views import indexPage, logoutUser

urlpatterns = [
    path("", indexPage, name="index"),
    path("logout/", logoutUser, name="logout"),
]
