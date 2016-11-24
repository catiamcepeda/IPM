from django import forms
from .models import Us, Tipo, Distrito, Concelho, Freguesia, Gruposintomas, Opcoesintomas

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['tipo']

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['distrito']

class ConcelhoForm(forms.ModelForm):
    class Meta:
        model = Concelho
        fields = ['concelho']

class FreguesiaForm(forms.ModelForm):
    class Meta:
        model = Freguesia
        fields = ['freguesia']

class USForm(forms.ModelForm):
    class Meta:
        model = Us
        fields = ['unidade']

class GruposintomasForm(forms.ModelForm):
    class Meta:
        model = Gruposintomas
        fields = ['gruposintomas']

class OpcoesintomasForm(forms.ModelForm):
    class Meta:
        model = Opcoesintomas
        fields = ['opcoes']