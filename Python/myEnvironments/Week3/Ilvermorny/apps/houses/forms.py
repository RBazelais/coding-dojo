from django import forms

class RegForm(forms.Form):
    name = forms.CharField(label="What is thine name?", max_length=254)
    email = forms.EmailField(label="How can we reach you via the interwebs")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password plz")