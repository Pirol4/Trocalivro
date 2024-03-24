from django.urls import path
from . import views

urlpatterns = [
    # direcionando do inicio para o index
    path('', views.index, name='index'),
    path('users/', views.index, name='index'),
    path('users/test', views.db_test, name='test'),
    path('users/books', views.list_books, name='books'),
]