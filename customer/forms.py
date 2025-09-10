from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    endereco = forms.CharField(max_length=255, required=True)
    cpf = forms.CharField(max_value=14, required=True, blank=False)
    telefone = forms.CharField(max_length=13, required=True, blank=False)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password1', 'endereco', 
                  'cpf', 'telefone']