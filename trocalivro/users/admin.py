from django.contrib import admin
from users.models import User, Book, Address


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Address)