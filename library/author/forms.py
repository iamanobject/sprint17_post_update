from .models import Author
from django.forms import ModelForm, TextInput


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'name'
            }),
            'surname': TextInput(attrs={
                'placeholder': 'surname'
            }),
            'patronymic': TextInput(attrs={
                'placeholder': 'patronymic'
            }),

        }
