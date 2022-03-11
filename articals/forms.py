from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Artical

class AddArticalForm(forms.ModelForm):
    class Meta:
        model = Artical
        fields = (
            'title',
            'author',
            'views',
            'text',
            'Date',
            'img')

        Widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'views': forms.TextInput(attrs={'class' : 'form-control'}),
            'Date': forms.DateInput(attrs={'class' : 'form-control'}),
            'img': forms.FileInput(attrs={'class' : 'form-control'}),
        }

