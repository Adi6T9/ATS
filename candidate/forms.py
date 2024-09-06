from django import forms
from .models import Candidate  # Adjust the import path based on your project structure

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'profile_picture',
            'full_name',
            'email',
            'phone_number',
            'resume',
            'cover_letter',
            'linkedin_profile',
            'date_of_birth',
            'address',
            'city',
            'state',
            'country'
        ]
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        
        email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))