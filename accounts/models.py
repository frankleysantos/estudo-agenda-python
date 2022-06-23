from django.db import models
from contatos.models import Contato
from django import forms
# Create your models here.

class FormContato(forms.ModelForm):
    # nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contato
        exclude = ('mostrar', 'data_criacao',)