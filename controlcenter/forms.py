from django import forms
from controlcenter.models import User


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "My Username"}))


class UserStatusForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['status']

    status = forms.ChoiceField(choices=User.STATUSES, widget=forms.Select(attrs={'class': 'form-control'}))

