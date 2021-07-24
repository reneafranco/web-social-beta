from django import forms
from django.forms import fields, widgets
from .models import Post, Comment, Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators


class Post_Form(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Add a Title....'
        })
    ),

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content']


class Comment_form(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Add a comment...'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']


class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.TextInput(attrs={'class': 'form-control'}),

            'password1': forms.TextInput(attrs={'class': 'form-control'}),

            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'web', 'picture']

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'web': forms.TextInput(attrs={'class': 'form-control'}),

        }