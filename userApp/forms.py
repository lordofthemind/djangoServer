from django import forms
from .models import UserModel

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'age', 'date_of_birth']
