from django.db import models
from django.utils import timezone

# Create your models here.
# sitter Model
class Sitter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, blank=False)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    education = models.CharField(max_length=255, blank=False, null=True)
    religion = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=200, blank=False, default= None)
    sitter_number = models.CharField(max_length=10, unique=True, blank=False, default=None)
    NIN = models.CharField(max_length=14, blank=False, null=True)

    
    # babys Model
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    baby_Number = models.IntegerField()
    baby_Bringer = models.CharField(max_length=100)
    parent_Name = models.CharField(max_length=100)
