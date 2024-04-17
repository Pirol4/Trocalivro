from django import forms

class RegisterUserForm(forms.Form):
    first_name = forms.CharField(help_text="Insira seu primeiro nome")
    last_name = forms.CharField(help_text="Insira seu sobrenome")
    email = forms.CharField(help_text="Insira seu email")
    phone_number = forms.CharField(help_text="Insira seu número de telefone")
    