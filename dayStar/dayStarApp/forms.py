from .models import *
from django.forms import ModelForm


# user forms
class Sitter_regForm(ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'