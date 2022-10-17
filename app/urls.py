from django.urls import path
from app.views import main,cadastro,cadastroRequest

urlpatterns = [
    path('', main, name='main-page'),
    path('cadastro', cadastro, name='cadastro'),
    path('submit_cadastro', cadastroRequest, name='cadastroRequest')
] 