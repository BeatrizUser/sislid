from django import forms
from .models import Pergunta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['nome', 'telefone', 'tipo', 'mensagem', 'bairro_sao_goncalo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
            'bairro_sao_goncalo': forms.Select(attrs={'class': 'form-select'}),
        }
