#!/usr/bin/env python3

from django.contrib.auth.models import AbstractUser
from tasks.models.base_model import BaseModel, models
from django.utils.translation import gettext as _


class CustomUser(AbstractUser, BaseModel):
    """
    User class
    """
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name=_('groups'),
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to their group(s).'
        ),
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name=_('user permissions'),
         help_text=_('Specific permissions for this user.'),
    )
    
    def __str__(self):
        return f'Welcome {self.username}'
    
    class Meta:
        db_table = 'users'