#!/usr/bin/env python3

from django.db import models
from uuid import uuid4
from datetime import datetime


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
    
    class Meta:
        abstract = True
    
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)
    
    @classmethod
    def find_obj(cls, **kwargs):
        query = cls.objects.filter(**kwargs).first()
        return query
    
    @classmethod
    def find_all_objs(cls, **kwargs):
        query = cls.objects.filter(**kwargs).all()
        return query
