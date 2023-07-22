from django import forms
from .models import Rfp

class CreateRfpForm(forms.ModelForm):
    class Meta:
        model = Rfp
        exclude = ['author']