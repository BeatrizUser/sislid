from django import forms
from .models import Pergunta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['nome', 'telefone', 'tipo', 'mensagem', 'bairro_sao_goncalo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'tipo': forms.Select(attrs={'class': 'form-select bg-light', 'placeholder': 'Tipo de Mensagem'}),
            'bairro_sao_goncalo': forms.Select(attrs={'class': 'form-select bg-light', 'placeholder': 'Seu Bairro'}),
            'mensagem': forms.TextInput(attrs={'class': 'form-control contact_form message_input', 'placeholder': 'Mensagem'}),
        }