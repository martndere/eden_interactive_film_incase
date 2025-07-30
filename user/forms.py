# forms.py
from django import forms
from .models import UserClip

class EditClipForm(forms.ModelForm):
    class Meta:
        model = UserClip
        fields = ['edit_start', 'edit_end']
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('edit_start')
        end = cleaned_data.get('edit_end')
        if start is not None and end is not None and (start < 0 or end <= start):
            raise forms.ValidationError("End time must be after start time and both must be positive.")
        return cleaned_data