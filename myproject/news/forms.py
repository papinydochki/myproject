from .models import Person
from django.forms import ModelForm, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'num_phone', 'e_mail']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "num_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "e_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            })
        }
