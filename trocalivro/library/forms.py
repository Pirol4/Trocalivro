from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=255, required=False)
    address = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'phone_number', 'address', 'password1', 'password2')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description','genre', 'image', 'status' )