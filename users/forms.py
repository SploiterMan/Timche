from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'phoneNumber')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('رمز ها مطابقت ندارند')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="شما نمیتوانید رمز خود را در  <a href=\"..password/\>این فرم</a> تغییر دهید")

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'phoneNumber', 'password', 'last_login')


