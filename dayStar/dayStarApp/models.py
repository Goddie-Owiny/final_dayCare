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
    STATUS_CHOICES = [
        (True, 'On Duty'),
        (False, 'Off Duty'),
    ]
    sitter_name = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=False)
    status = models.BooleanField(choices=STATUS_CHOICES, null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    
    def __str__(self):
        return self.sitter_name.name

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

    PERIOD_CHOICES = [
    ("Full Day", "Full Day"),
    ("Half Day", "Half Day"),
    ]



    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0, null=True, blank=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default="Male")
    location = models.CharField(max_length=100)
    period_of_stay = models.CharField(max_length=100, choices=PERIOD_CHOICES, null=True, blank=True)
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

# baby payment model
class BabyPayment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    period_of_stay = models.ForeignKey(Period, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0, choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '45000')], null= True, blank=True)
    date_of_payment = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    duration_of_pay = models.CharField(max_length=100, choices=[("Half day", "Half day"), ("Full Day", "Full Day"), ("Monthly Full Day", "Monthly Full Day"),("Monthly Half Day", "Monthly Half Day")])
    amount_paid = models.IntegerField(default=0,) 
    
    
    def __str__(self):
        return f"{self.baby} {self.period_of_stay}"
    
    def change(self):
        recieved = self.amount - self.amount_paid
        return int(recieved)

class SitterPayment(models.Model):
    sitter = models.ForeignKey(Sitter_on_duty, on_delete=models.CASCADE, null=True, blank=True)
    num_of_baby = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=3000)

    def sitterpay(self):
        total_pay = self.num_of_baby * self.amount_paid
        return int(total_pay)

class AddItem(models.Model):
    doll_name = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.doll_name

class ItemSelling(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    doll_name = models.CharField(max_length=100, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
   
    def total_amount(self):
        total = self.quantity * self.price
        return int(total)
    
    def get_change(self):
        # Check if amount_paid is None
        if self.amount_paid is None:
            return None
        
        # Otherwise, proceed with the calculation
        change = self.total_amount() - self.amount_paid
        return change
    
      