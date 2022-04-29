from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Artical, Category

#choices = [('coding'), ('coding'), ('hello'), ('hello'), ('test'),('test')
def c():
        
    choices = Category.objects.all().values_list('name','name')

    choice_list = []

    for item in choices:
        choice_list.append(item)
    return choice_list
class AddArticalForm(forms.ModelForm):
    category = forms.ChoiceField(choices=c)
    class Meta:
        model = Artical
        fields = (
            'title',
            'category',
            'author',
            'text',
           
            'img')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control '}),
            'author': forms.TextInput(attrs={'class' : 'form-control ', 'value':'', 'id':'user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class' : 'form-control'}),
            'category': forms.Select(attrs={'class' : 'form-control'}),
            # 'views': forms.TextInput(attrs={'class' : 'form-control'}),
            'text': forms.Textarea(attrs={'class' : 'form-control'}),
           # 'Date': forms.DateInput(attrs={'class' : 'form-control'}),
            'img': forms.FileInput(attrs={'class' : 'form-control'}),
        }



class UpdateArtical(forms.ModelForm):
    category = forms.ChoiceField(choices=c)
    class Meta:
        model = Artical
        fields = (
            'title',
            'category',
            'text',
            
            'img')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control '}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'category': forms.Select(attrs={'class' : 'form-control'}),
            # 'views': forms.TextInput(attrs={'class' : 'form-control'}),
            'text': forms.Textarea(attrs={'class' : 'form-control'}),
            #'Date': forms.DateInput(attrs={'class' : 'form-control'}),
            'img': forms.FileInput(attrs={'class' : 'form-control'}),
        }
class InputForm(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())