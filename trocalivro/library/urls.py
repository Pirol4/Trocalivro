from django.urls import path, include
from library import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book_add, name='book-add'), # Implementar
    path('book/<int:id>', views.book_detail_view, name='book-detail'),
    path('profile/', views.profile, name='users-profile'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))
]