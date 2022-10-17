from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Seu nome"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Seu Email"
        })
    )
    password = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Sua Senha"
        })
    )