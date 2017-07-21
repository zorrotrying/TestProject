from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Model_cdap(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
