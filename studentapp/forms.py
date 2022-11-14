from django.db import models
from django import forms
from .models import Student
# from django.core.exceptions import ValidationError
from studentapp.validators import age_validation


# Create your models here.

class  StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

# choice=[('---','---'),('+1','+1'),('+2','+2')]

# class StudentForm(forms.Form):
#     Full_Name=forms.CharField(label="Full Name ",max_length=50)
#     Email = forms.EmailField(max_length=100)
#     Age = forms.IntegerField(validators=[age_validation])
#     Class =forms.ChoiceField(choices = choice,default='---')
#     Description= forms.TextField(max_length=400,required=False,initial="Description of Student, if any...") 

   
        