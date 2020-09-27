from django import forms
from django.db import models
from django.contrib.auth.forms import User


class changeEmailForm(forms.Form):

    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "value": "", "placeholder": "Current Email"
    }))
    email2 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "Email New"
    }))
    email3 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "Repet Email New"
    }))

    class Meta():
        model = User
        filter = ["email"]


class changePassForm(forms.Form):
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Current Password"
    }))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "New Password"
    }))
    password3 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        "class": "input-field", "placeholder": "Repet New Password"
    }))

    class Meta():
        model = User
        filter = ['password']


class changeUsernameForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Current Username"}))
    username2 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "New Username"}))
    username3 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "Repet New Username"}))

    class Meta():
        model = User
        filter = ['username']
