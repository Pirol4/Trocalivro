from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:id>', views.book_detail_view, name='book-detail')
]