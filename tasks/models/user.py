#!/usr/bin/env python3

from django.contrib.auth.models import AbstractUser
from models.base_model import BaseModel, models


class User(AbstractUser, BaseModel):
    """
    User class
    """
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'Welcome {self.username}'
    
    class Meta:
        db_table = 'users'