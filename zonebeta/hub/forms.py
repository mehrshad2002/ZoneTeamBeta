from django import forms
from .models import Hubmodel
class HubformItems(forms.ModelForm):
    class Meta:
        model= Hubmodel
        fields = ['title','content']
class HubForms(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your task title"}))
    content = forms.CharField(required=False,
              widget=forms.Textarea(attrs={"rows":20,'cols':120}))