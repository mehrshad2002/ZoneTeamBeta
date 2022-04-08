from django import forms

class HubForms(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=500)