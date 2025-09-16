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

        if start is not None and start < 0:
            self.add_error('edit_start', "Start time cannot be negative.")

        if end is not None and end < 0:
            self.add_error('edit_end', "End time cannot be negative.")

        if start is not None and end is not None and end <= start:
            self.add_error('edit_end', "End time must be after the start time.")
            
        return cleaned_data