from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label='ایمیل'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه ی عبور'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
        label='تکرار کلمه عبور'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already taken')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError('passwords do not match')
        return password2