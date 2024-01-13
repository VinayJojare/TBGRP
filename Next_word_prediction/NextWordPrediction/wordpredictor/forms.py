# wordpredictor/forms.py
from django import forms
from .models import CaptureData, TrainingData

class TrainingDataForm(forms.ModelForm):
    class Meta:
        model = TrainingData
        fields = ['sentence']

class CaptureDataForm(forms.ModelForm):
    class Meta:
        model = CaptureData
        fields = ['sentence', 'next_word']
