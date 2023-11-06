#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    User class
    """
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'Welcome {self.username}'
    
    