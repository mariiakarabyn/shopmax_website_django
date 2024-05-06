from django.views.generic import FormView

from . forms import ContactForm
from . models import Contact


class ContactUsView(FormView):
    template_name = 'contact.html'
    model = Contact
    success_url = '/contact/'
    form_class = ContactForm
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    