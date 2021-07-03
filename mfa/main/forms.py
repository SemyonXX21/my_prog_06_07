from .models  import Lucoshko
from django.forms import ModelForm, TextInput



class LucoshkoForm(ModelForm):
    class Meta:
        model = Lucoshko
        fields = ['name', 'telephone', 'address', 'product', 'quantity']
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введи имя'
        }),
            'telephone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи телефон'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи адрес'
            }),
            'product': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи продукт'
            }),
            'quantity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи количество'
            }),

        }

