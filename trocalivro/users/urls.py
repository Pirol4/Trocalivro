from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/test', views.db_test, name='test'),
]