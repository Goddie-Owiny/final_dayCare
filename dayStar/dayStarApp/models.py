from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from datetime import datetime

# Create your models here.
# sitter Model
class Sitter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    age = models.PositiveIntegerField(default=1, blank=False)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=13, validators=[MinLengthValidator(10)])
    education_Level = models.CharField(max_length=255, blank=False, null=True)
    religion = models.CharField(max_length=100, blank=True)
    next_of_kin = models.CharField(max_length=200, blank=False, default= None)
    recommended_by = models.CharField(max_length=100, null=True, blank=True)
    sitter_number = models.CharField(max_length=10, unique=True, blank=False, default=None)
    # date_of_registration = models.DateTimeField(null=True, blank=False, default=timezone.now)
    NIN = models.CharField(max_length=14, blank=False, null=True)

    def __str__(self):
        return self.name
    
class Sitter_on_duty(models.Model):
    sitter_name = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=False)
    status = models.CharField(choices=[('on_duty', 'on_duty')], max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    
    def __str__(self):
        return self.sitter_name

class Period(models.Model):
    period = models.CharField(max_length=100, default="Full Day")
    def __str__(self):
        return self.period
    
    
    # babys Model
class Baby(models.Model):
    GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0, null=True, blank=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default="Male")
    location = models.CharField(max_length=100)
    period_of_stay = models.CharField(max_length=100, null=True, blank=True, default="Full Day")
    baby_Number = models.IntegerField()
    brought_by = models.CharField(max_length=100)
    parent_Name = models.CharField(max_length=100)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.TimeField(null=True, blank=True)
    brought_by = models.CharField(max_length=100)
    status = models.BooleanField(null=True, blank=True,  default=False)
    assigned_to = models.ForeignKey(Sitter_on_duty, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    period_of_stay = models.ForeignKey(Period, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null= True, blank=True)
    date_of_payment = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ItemSelling(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=False, blank=False)
    item = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, )
    quantity = models.IntegerField(default=1, null=False)

    def total_amount(self):
        return self.price * self.quantity
    

class AddItem(models.Model):
    item = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=1, null=False)
    