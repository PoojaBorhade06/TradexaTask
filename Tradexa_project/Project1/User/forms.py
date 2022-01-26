from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError((f'{value} is registered already'),params={'value':value})


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email=forms.EmailField(validators=[validate_email])
    class Meta:
        model=User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

    def __str__(self):
        return f'{self.username}'
