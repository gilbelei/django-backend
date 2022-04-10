from django.contrib import admin

from .models import Categoria, Curso


class CategoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ...
