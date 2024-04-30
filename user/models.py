from django.db import models
from django.contrib.auth.models import User

from book.models import Book


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
