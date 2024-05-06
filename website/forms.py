from django import forms

from . models import Contact


class ContactForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True
            
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email", "message")
        required = ("first_name", "last_name", "email", "message")
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Please enter your message', 'maxlength': 1000}),
        }
        
