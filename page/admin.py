from django.contrib import admin
from .models import Categoria, Entradas, Saidas

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Entradas)
admin.site.register(Saidas)