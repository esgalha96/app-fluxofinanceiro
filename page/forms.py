from django import forms
from .models import Entradas, Saidas, Categoria
from acesso.models import Usuario

class EntradasForm(forms.ModelForm):

    def __init__(self, id_usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = Usuario.objects.filter(id=id_usuario)
        self.fields['usuario'].initial = Usuario.objects.filter(id=id_usuario).first()
        self.fields['usuario'].disabled = True
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=Usuario.objects.filter(id=id_usuario).first())

    class Meta:
        model = Entradas
        fields = "__all__"

class SaidasForm(forms.ModelForm):

    def __init__(self, id_usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = Usuario.objects.filter(id=id_usuario)
        self.fields['usuario'].initial = Usuario.objects.filter(id=id_usuario).first()
        self.fields['usuario'].disabled = True
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=Usuario.objects.filter(id=id_usuario).first())

    class Meta:
        model = Saidas
        fields = "__all__"

class CategoriasForm(forms.ModelForm):

    def __init__(self, id_usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = Usuario.objects.filter(id=id_usuario)
        self.fields['usuario'].initial = Usuario.objects.filter(id=id_usuario).first()
        self.fields['usuario'].disabled = True
        
    class Meta:
        model = Categoria
        fields = "__all__"