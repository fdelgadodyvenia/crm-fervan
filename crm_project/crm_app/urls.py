from django.urls import path
from . import views

urlpatterns = [
    path('name/', views.get_name, name='get_name'),
    path('list/', views.list_clients, name='list_clients'),
]
