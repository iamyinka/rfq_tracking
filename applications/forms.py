from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['concept_note']
        # exclude = "['rep', 'approved_by', 'reviewed_by', 'status', 'submission_date']"
        # exclude = ['rep', 'approved_by', 'reviewed_by', 'status', 'submission_date']



        