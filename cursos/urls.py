from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos/categoria/<int:categoria_id>/',
         views.categoria, name="categoria"),
    path('cursos/<id>/', views.curso, name="curso"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
