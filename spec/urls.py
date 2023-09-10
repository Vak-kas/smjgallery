from django.urls import path

from . import views;

app_name = 'spec'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/spec', )
]
