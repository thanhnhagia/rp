# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dashboard(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    dashboard_father = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:70]
