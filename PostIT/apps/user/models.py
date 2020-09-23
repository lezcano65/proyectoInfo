from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class nota(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=400)
    fecha = models.DateField()
    color = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo
