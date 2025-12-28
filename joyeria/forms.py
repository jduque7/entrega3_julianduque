from django import forms
from .models import Categoria, Material, Joya


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__' 


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class JoyaForm(forms.ModelForm):
    class Meta:
        model = Joya
        fields = '__all__'