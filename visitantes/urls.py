from django.urls import path

from . import views

urlpatterns = [
    path('registro/', views.register_view, name='registro'),
]
