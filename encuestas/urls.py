from django.urls import path
from . import views

urlpatterns = [
    path('', views.encuestas, name='encuestas'),
]