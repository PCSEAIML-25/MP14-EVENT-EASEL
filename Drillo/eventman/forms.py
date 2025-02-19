from django import forms
from .models import FormSubmission


class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ('name', 'email', 'shortDesc', 'message', 'start_date', 'end_date', 'url', 'about', 'crousel', 'sponsors')
        labels = {
            'start_date': 'Registration Start Date',
            'end_date': 'Registration End Date',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Event Name"
            }),
            'email': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Enter your Email"
            }),
            'shortDesc': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Small Description about event"
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Brief Details about event"
            }),
            'start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'end_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'url': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Event Site URL (should match Event Name)"
            }),
            'about': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "About Image Link"
            }),
            'crousel': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Paste Images Links seperated with comma"
            }),
            'sponsors': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-300 transition-colors',
                'placeholder': "Paste Images Links seperated with comma"
            }),
        }
