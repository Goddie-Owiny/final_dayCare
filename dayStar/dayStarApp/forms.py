from .models import *
from django import forms

class Sitter_regForm(forms.Form):
    name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    age = forms.IntegerField(widget= forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    gender = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    location = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    contact = forms.CharField(max_length=13, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    education_Level = forms.CharField(max_length=255, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    religion = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    next_of_kin = forms.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    recommended_by = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    # date_of_registration = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    sitter_number = forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)
    NIN = forms.CharField(max_length=14, widget= forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        age = cleaned_data.get('age')
        gender = cleaned_data.get('gender')
        location = cleaned_data.get('location')
        contact = cleaned_data.get('contact')
        education_Level = cleaned_data.get('education_Level')
        religion = cleaned_data.get('religion')
        next_of_kin = cleaned_data.get('next_of_kin')
        recommended_by = cleaned_data.get('recommended_by')
        # date_of_registration = cleaned_data.get('date_of_registration')
        sitter_number = cleaned_data.get('sitter_number')
        NIN = cleaned_data.get('NIN')

        if not name:
            self.add_error('name', 'Please provide a Name')
        elif len(name) < 3: 
            self.add_error('name', 'Name must be at least 3 characters')

        if not age:
            self.add_error('age', 'Please provide your age')

        # if age < 18 or age > 40:
        #     self.add_error('age', 'Age must be between 18 and 40')

        if not gender:
            self.add_error('gender', 'Please provide specify your Gender')
        
        if not location:
            self.add_error('location', 'Please provide sitter location')
        
        if not contact:
            self.add_error('contact', 'Please provide telephone number')
        
        if not education_Level:
            self.add_error('education_Level', 'Please Enter Education Level')
        
        if not next_of_kin:
            self.add_error('next_of_kin', 'Provide a next of kin')
        
        if not recommended_by:
            self.add_error('recommended_by', 'Specify who recommended you')
        
        if not sitter_number:
            self.add_error('sitter_number', 'Provide a unique sitter number')
        
        if not NIN:
            self.add_error('NIN', 'provide the sitter`s NIN')

        return cleaned_data
        


class Baby_regForm(forms.Form):
        GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
        
        # PERIOD_CHOICES = Period.period

    
        name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
        gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        location = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        #period_of_stay = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'form-control'}))
        baby_Number = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        brought_by = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        parent_Name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))        
        # time_out = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
        status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            age = cleaned_data.get('age')
            gender = cleaned_data.get('gender')
            location = cleaned_data.get('location')
            period_of_stay = cleaned_data.get('period_of_stay')
            baby_Number = cleaned_data.get('baby_Number')
            brought_by = cleaned_data.get('brought_by')
            parent_Name = cleaned_data.get('parent_Name')
            time_out = cleaned_data.get('time_out')
            status = cleaned_data.get('status')


        # if not name or not age or not gender or not location or not period_of_stay or not baby_Number or not brought_by or not parent_Name or not time_out:
        #     self.add_error('name', 'Fields required')

       
        
class Sales_regForm(forms.Form):
    class Meta:
        model = Sale
        fields = '__all__'