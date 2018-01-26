from django import forms
# from django.contrib.auth import get_user_model
from models import NewUser

class RegisterForm(forms.Form):
    name = forms.CharField(max_length = 254)
    alias = forms.CharField(max_length = 254)
    email = forms.EmailField(max_length = 254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = NewUser()
        fields = ('name', 'alias', 'email', 'password','confirm_password')

    def __str__(self):
        name = self.name

# class LoginForm(forms.ModelForm):
#     email = forms.EmailField(max_length = 254)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User()
#         fields = ('email', 'password')

#     def __str__(self):
#         email = self.email