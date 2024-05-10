from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit

# user forms
class Sitter_regForm(ModelForm):
    class Meta:
        model = Sitter
        fields = ['gender']
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
        )


class Baby_regForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'


class Item_sellForm(ModelForm):
    class Meta:
        model = ItemSelling
        fields = '__all__'


class Item_regForm(ModelForm):
    class Meta:
        model = AddItem
        fields = '__all__'

class Payment_regForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
