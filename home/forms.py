from django import forms
from .models import *
from django.contrib.auth.models import User

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


