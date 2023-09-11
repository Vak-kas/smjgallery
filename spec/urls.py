from django.urls import path, include
from . import views



app_name = 'spec';

urlpatterns = [
    # path('', views.index, name="index"),
    path('create/', views.create_spec, name="create_spec"),
    path('', views.ActivityListCreateAPIViews.as_view(), name="activity-list-create")
]
