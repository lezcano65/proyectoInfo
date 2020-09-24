from django.urls import path
from .views import *

urlpatterns = [
    path("home/", mostrar_notas, name="home"),
    path("edit/", edit, name="edit"),
    path("create/", newnota, name="create"),
    path("configuracion/", configuracion, name="configuracion"),
    path("deleteNote/", deleteNote, name="delete"),
    path("informatorio/", informatorio, name="informatorio"),
]
