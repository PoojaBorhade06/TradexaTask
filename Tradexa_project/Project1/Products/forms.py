from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

        widgets = {
            'created_at': forms.NumberInput(attrs={'type': 'date'}),
            'updated_at': forms.NumberInput(attrs={'type': 'date'}),
            }

