from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('graph', views.graph, name='graph'),
]