# sendemail/forms.py
from django import forms
from services.models import Service
from django.forms import ModelForm

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ServiceForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = False
        self.fields['image'].required = False
