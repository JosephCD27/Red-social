from django.db import models

class User(models.Model):
    usuario_nombre = models.TextField(blank=True, null=True, name="Nombre Usuario",max_length=100)
    usuario_apellido = models.TextField(blank=True, null=True, name="Apellido Usuario",max_length=100)
    usuario_alias = models.TextField(blank=True, null=True, name="Alias Usuario",max_length=100)



