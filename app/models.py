from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128, blank=True)

class Quote(models.Model):
    book = models.ForeignKey(Book)
    text = models.TextField()

class Location(models.Model):
    book = models.ForeignKey(Book)
    label = models.CharField(max_length=64, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
