from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.
# sitter Model
class Sitter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(default=1, blank=False)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=13, validators=[MinLengthValidator(10)])
    education_Level = models.CharField(max_length=255, blank=False, null=True)
    religion = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=200, blank=False, default= None)
    recommended_by = models.CharField(max_length=100, null=True, blank=True)
    sitter_number = models.CharField(max_length=10, unique=True, blank=False, default=None)
    NIN = models.CharField(max_length=14, blank=False, null=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    period = models.CharField(max_length=100, null=True, blank=False)
    def __str__(self):
        return self.period
    
    
    # babys Model
class Baby(models.Model):
    GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default="Male")
    location = models.CharField(max_length=100)
    period_of_stay = models.ForeignKey(Period, on_delete=models.CASCADE, blank=False, null=True, default=0)
    baby_Number = models.IntegerField()
    brought_by = models.CharField(max_length=100)
    parent_Name = models.CharField(max_length=100)

class Sale(models.Model):
    item = models.CharField(max_length=100, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=1, null=False)

    def total_price(self):
        return self.price * self.quantity