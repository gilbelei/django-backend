from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos/<id>/', views.curso, name="curso"),
]
