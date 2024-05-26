from django.urls import path
from . import views

urlpatterns = [
    path('name/', views.insert_client, name='insert_client'),
    path('list/', views.list_clients, name='list_clients'),
]
