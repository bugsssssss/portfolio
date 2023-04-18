from django import forms
from .models import *


class CallbackForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Name'}))
    topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 5, 'resize': 'none'}))

    class Meta:
        model = Callback
        fields = '__all__'
