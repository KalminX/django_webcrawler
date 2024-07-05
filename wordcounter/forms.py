from django.forms import EmailField
from django import forms
from .models import *


class InputForm(forms.ModelForm):
    url = EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Any URL.....'}))

    class Meta:
        model = Mail  #
        fields = ['url']
