from django.contrib import admin
from library.models import User, Book


# Registrando os modelos.
admin.site.register(User)
admin.site.register(Book)