from django import forms
from .models import Donor


class AddDonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        exclude = ['user']