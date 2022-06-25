from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User
from .choice import *

class CustomUserChangeForm(UserChangeForm):
    password = None
         
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',}), 
    )        
    student_id = forms.IntegerField(required=False, label='학번', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'maxlength':'8', 'oninput':"maxLengthCheck(this)",}), 
    )
    grade = forms.ChoiceField(choices=GRADE_CHOICES, label='학년', widget=forms.Select(
        attrs={'class': 'form-control',}), 
    )
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, label='학과', widget=forms.Select(
        attrs={'class': 'form-control',}), 
    )
       
    
