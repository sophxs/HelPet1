from django.shortcuts import render
from django.shortcuts import render
from .forms import UserForm
from .models import User

def main(request):
    return render(request, 'index.html', {})

def cadastro(request):
    return render(request, 'cadastro.html', {})

def cadastroRequest(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            u = User(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            u.save()
        else:
            return cadastro(request)
    return main(request)