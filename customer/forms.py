from django import forms
from .models import CustomerModel
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm

class CustomerCreationForm(UserCreationForm):
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = CustomerModel
        fields = [
            'username', 'email', 'cpf', 'nome_rua', 'numero_residencia', 'nome_bairro','nome_cidade', 'telefone', 'foto_perfil', 'password1', 'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF (apenas números)'}),
            'nome_rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Rua'}),
            'numero_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero da residencia'}),
            'nome_bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'nome_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme a senha'})


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome de usuário' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Senha'}))

class CustomerUpdateForm(forms.ModelForm):
    """Formulário para editar perfil do usuário"""
    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'email', 'foto_perfil', 'nome_rua', 'numero_residencia', 'nome_bairro', 'nome_cidade', 'telefone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'nome_rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da rua'}),
            'numero_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero da residencia'}),
            'nome_bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'nome_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'foto_perfil': 'Foto de Perfil',
            'nome_rua': 'Rua',
            'numero_residencia': 'Numero da residencia',
            'nome_bairro': 'Bairro',
            'nome_cidade': 'Cidade',
            'telefone': 'Telefone',
        }