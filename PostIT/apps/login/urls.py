from django.urls import path
#from Login import views
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout, name="logout"),
]
