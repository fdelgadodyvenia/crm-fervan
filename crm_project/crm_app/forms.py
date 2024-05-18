from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
