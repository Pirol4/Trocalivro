from django.db import models
from django.utils import timezone
from django.urls import reverse 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum
from datetime import datetime
import uuid


class StatusBook(Enum):
  AVAILABLE = 'Available'
  IN_EXCHANGE = 'In Exchange'
  UNAVAILABLE = 'Unavailable'


class Profile(models.Model):
  user = models.OneToOneField(User, related_name='profile', on_delete = models.CASCADE, null=True)
  firstname = models.CharField(max_length = 255)
  lastname = models.CharField(max_length = 255)
  email = models.EmailField(default = "", null = True)
  phone_number = models.CharField(max_length = 255,default = "")
  reputation = models.IntegerField(default = 5) 
  address = models.TextField(default = "")

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()
    
  # @receiver(post_save, sender=User)
  # def update_user_profile(sender, instance, created, **kwargs):
  #   if created:
  #       Profile.objects.create(user=instance)
  #   instance.profile.save()

class Book(models.Model):
  title = models.CharField(max_length = 255)
  description = models.TextField()
  genre = models.CharField(max_length=200, default = "", null = True)
  image = models.ImageField(upload_to='library/static/images/', blank=True, null=True)
  status = models.CharField(max_length = 20, choices = [(tag.name, tag.value) for tag in StatusBook])
  
  created_at = models.DateField(default=timezone.now)
  owner = models.ForeignKey(Profile, on_delete = models.CASCADE)

  def get_absolute_url(self):
    return reverse('book-detail', args=[str(self.id)])
