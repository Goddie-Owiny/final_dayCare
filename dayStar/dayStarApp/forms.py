from .models import *
from django.forms import ModelForm
from django import forms


# user forms
class Sitter_regForm(ModelForm):
    class Meta:
        model = Sitter
        fields = ['gender']
        widgets = {                         # widgets for user form choices
            'gender': forms.Select(choices = Baby.GENDER_CHOICES),
        }
        fields = '__all__'


class Baby_regForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'


class Sales_regForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'