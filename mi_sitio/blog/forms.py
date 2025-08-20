from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
        }
