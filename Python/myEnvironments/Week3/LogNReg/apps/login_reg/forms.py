from django import forms
from models import User

class RegForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='First Name:', required=True)
    last_name = forms.CharField(max_length=20, label='Last Name:', required=True)
    email = forms.EmailField(max_length=50, label='Email:', required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password plz")
