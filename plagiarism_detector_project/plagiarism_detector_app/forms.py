# plagiarism_detector_app/forms.py
from django import forms
from .models import TextComparison

class TextComparisonForm(forms.ModelForm):
    class Meta:
        model = TextComparison
        fields = ['original_text', 'suspicious_text']
