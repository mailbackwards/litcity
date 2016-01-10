from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return self.name

class Quote(models.Model):
    book = models.ForeignKey(Book)
    text = models.TextField()
    approved = models.BooleanField(default=True)

    def __unicode__(self):
        return self.text[:140]

class Location(models.Model):
    book = models.ForeignKey(Book)
    label = models.CharField(max_length=64, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
    quotes = models.ManyToManyField(Quote, related_name='locations', blank=True)
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label
