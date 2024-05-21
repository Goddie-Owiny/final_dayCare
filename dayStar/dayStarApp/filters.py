import django_filters
from . models import *

from django import forms

class BabyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(widget=forms.TextInput(attrs={'placeholder': 'Search Baby By Name'}))


    class Meta:
        model = Baby
        fields = ['name']
        
