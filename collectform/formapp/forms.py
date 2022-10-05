from dataclasses import field
from pyexpat import model
from django import forms
from formapp.models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        models = Candidate
        fields = "__all__"
