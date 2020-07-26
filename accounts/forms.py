from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DateTimePickerInput
from django.forms import ModelForm
from .models import Classes


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = { 'username': forms.TextInput(attrs={'placeholder':'Username'}),
                    'password1': forms.PasswordInput(attrs={'placeholder':'Password'}),
                    'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
                    }

class ClassesForm(forms.Form):
    classes = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Class name'}))
    teacher = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Teacher\'s name'}))
    subject = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Subject'}))

class NotesForm(forms.Form):
    title = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Title','class':'uploadinput'}))
    file = forms.FileField(label='Upload File',required=False)
    desc = forms.CharField(required = False,widget=forms.Textarea(attrs={'placeholder':'Description','class':'uploadinput'}))

class AssignmentForm(forms.Form):
    title = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Title','class':'uploadinput'}))
    file = forms.FileField(label='Upload File',required=False)
    desc = forms.CharField(required = False,widget=forms.Textarea(attrs={'placeholder':'Description','class':'uploadinput'}))
    last_date=forms.DateTimeField(label="Submission Date",widget=DateTimePickerInput())
    max_marks = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Maximum Marks', 'class': 'uploadinput'}))