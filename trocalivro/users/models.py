from django.db import models
from django.utils import timezone
from enum import Enum
from datetime import datetime
import uuid


class StatusBook(Enum):
  AVAILABLE = 'Available'
  IN_EXCHANGE = 'In Exchange'
  UNAVAILABLE = 'Unavailable'

class User(models.Model):
  firstname = models.CharField(max_length = 255)
  lastname = models.CharField(max_length = 255)
  email = models.EmailField(default = "", null = True)
  phone_number = models.CharField(max_length = 255,default = "")
  reputation = models.IntegerField(default = 5) 
  address = models.TextField(default = "")

class Book(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length = 255)
  description = models.TextField()
  genre = models.CharField(max_length=200, default = "", null = True)
  image = models.ImageField(upload_to='books-mages/', blank=True, null=True)
  status = models.CharField(max_length = 20, choices = [(tag.name, tag.value) for tag in StatusBook])
  
  created_at = models.DateField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete = models.CASCADE)
  






