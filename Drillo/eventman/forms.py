from django import forms
from .models import FormSubmission

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ('name', 'email', 'shortDesc', 'message', 'start_date', 'end_date', 'url', 'about', 'crousel', 'sponsors')
        labels = {
            'start_date' : 'Registration Start Date',
            'end_date' : 'Registration End Date',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Event Name"}),
            'email': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Enter your Email"}),
            'shortDesc': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Small Description about event"}),
            'message': forms.Textarea(attrs={"rows": 5, 'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', 'placeholder': "Brief Details about event"}),
            'start_date': forms.DateInput(format=('%d/%m/%Y'),
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Select a date',
                                                 'type': 'date'
                                                 }),
            'end_date': forms.DateInput(format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'
                                               }),
            'url': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Event Site URL"}),

            'about': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "About Image Link"}),

            'crousel': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Crousel Images Link seperated by Commas"}),
            
            'sponsors': forms.TextInput(attrs={'class': 'border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2', "placeholder": "Sponsors Logos Link seperated by commas"}),
        }
