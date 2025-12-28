from django.contrib import admin
from .models import Categoria, Material, Joya


class JoyaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'peso_gramos', 'stock')

admin.site.register(Categoria)
admin.site.register(Material)
admin.site.register(Joya, JoyaAdmin)