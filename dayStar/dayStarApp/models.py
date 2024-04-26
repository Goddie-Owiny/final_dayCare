from django.db import models
from django.utils import timezone

# Create your models here.
# sitter Model
class Sitter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, blank=False)
    gender = models.CharField(max_length=100)

    # babys Model
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    babyNum = models.IntegerField()
    babyBringer = models.CharField(max_length=100)
    parentName = models.CharField(max_length=100)
