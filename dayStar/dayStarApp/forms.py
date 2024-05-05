from .models import *
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit

# user forms
class Sitter_regForm(ModelForm):
    class Meta:
        model = Sitter
        fields = ['gender']
        widgets = {                         # widgets for user form choices
            'gender': forms.Select(choices = Baby.GENDER_CHOICES),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Sitter_regForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                Div('name', css_class='col-md-5'),
                Div('gender', css_class='col-md-5'),
                Div('education_Level', css_class='col-md-5'),
                Div('contact', css_class='col-md-5'),
                Div('sitter_number', css_class='col-md-5'),
                css_class='row',
            ),
            Fieldset(
                Div('NIN', css_class='col-md-5'),
                Div('name', css_class='col-md-5'),
                Div('recommended_by', css_class='col-md-5'),
                Div('next_of_kin', css_class='col-md-5'),
                Div('location', css_class='col-md-5'),
                css_class='row',
            ),
            # Submit('submit', 'Submit', css_class='btn btn-primary'),
        )


class Baby_regForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'


class Sales_regForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'