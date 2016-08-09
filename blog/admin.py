from django.contrib import admin
from .models import Post #importamos el modelos Post, creado al administrador de Django.

# Register your models here. Registramos nuestro modelo recien creado Post
admin.site.register(Post)
