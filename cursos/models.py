from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)
    type = models.CharField(max_length=65)


class Curso(models.Model):
    title = models.CharField(max_length=65)
    short_description = models.CharField(max_length=165)
    time_description = models.CharField(max_length=65)
    hours_description = models.CharField(max_length=65)
    long_description = models.TextField()
    description_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover_tumb = models.ImageField(upload_to='cursos/covers/tumb/%Y/%m/%d/')
    cover = models.ImageField(upload_to='cursos/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    people = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
