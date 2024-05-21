from django.forms import ModelForm
from .models import *
from django import forms
from datetime import datetime

# user forms
class Sitter_regForm(ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    
    # def clean_date_of_birth(self):
    #     date_of_birth = self.cleaned_data.get('date_of_birth')
    #     if date_of_birth > datetime.today().date():
    #         raise forms.ValidationError("Date of birth can't be in the future.")    # Check if date_of_birth is in the future




class Baby_regForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'
        widgets = {
            'time_out': forms.TimeInput(attrs={'type': 'time'}),
            'status': forms.CheckboxInput(),
        }



class Item_sellForm(forms.ModelForm):   # item sellling form
    class Meta:
        model = ItemSelling
        fields = ['baby', 'quantity', 'price', 'amount_paid']


class Item_regForm(ModelForm):       # item registration form
    class Meta:
        model = AddItem
        fields = '__all__'

class BabyPaymentForm(ModelForm):   #baby payment form
    class Meta:
        model = BabyPayment
        fields = '__all__'

class SitterPaymentForm(ModelForm):   #Sitter payment form
    class Meta:
        model = SitterPayment
        fields = '__all__'

    
   

class Sitter_dutyForm(forms.ModelForm):   # sitter duty form
    class Meta:
        model = Sitter_on_duty
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.CheckboxInput(),
        }


class Addmore(ModelForm):  #adding item form
    class Meta:
        model = AddItem
        fields = ['quantity']      



class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue_Stock
        fields = '__all__'
        widgets = {
            'date_of_issue': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AddexistingStock(ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity']