from django.db import models
from enum import Enum


# Classe Enum para verificar o status de um livro
class StatusBook(Enum):
  AVAILABLE = 'Available'
  IN_EXCHANGE = 'In Exchange'
  UNAVAILABLE = 'Unavailable'


# Tabela do usuário
class User(models.Model):
  firstname = models.CharField(max_length = 255)
  lastname = models.CharField(max_length = 255)
  email = models.EmailField(default = "", null = True)
  phone_number = models.CharField(max_length = 255,default = "")
  reputation = models.IntegerField(default = 5) 

  def __str__(self):
    return f'user = {self.firstname}, email = {self.email}, reputation = {self.reputation}'


# Tabela dos endereços 
class Address(models.Model):
  owner_address = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
  # owner = models.ForeignKey(User, on_delete=models.CASCADE)
  street = models.CharField(max_length = 255)
  number = models.CharField(max_length = 255)
  complement = models.CharField(max_length = 255)
  city = models.CharField(max_length = 255)
  country = models.CharField(max_length = 255)
  zip_code = models.CharField(max_length = 255)

  def __str__(self):
    return f'street = {self.street}, complement = {self.complement}, city = {self.city}, country = {self.country}'
    


# Tabela livro
class Book(models.Model):
  owner = models.ForeignKey(User, on_delete = models.CASCADE)
  status = models.CharField(max_length = 20, choices = [(tag.name, tag.value) for tag in StatusBook])
  name = models.CharField(max_length = 255)
  description = models.TextField()
  # image = models.ImageField(upload_to='books/', blank=True, null=True)

  def __str__(self):
    return f'book = {self.name}, description = {self.description}, status = {self.status}, owner = {self.owner.firstname}'







