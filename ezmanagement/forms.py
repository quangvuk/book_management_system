from django import forms
from api.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'is_superuser', 'email', 'is_staff', 'is_active')
