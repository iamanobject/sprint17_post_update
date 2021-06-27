from .models import CustomUser
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'password',
        ]
