from django import forms
from .models import Manga

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['name', 'description', 'rating', 'photo']

        widgets = {
            'title': forms.TextInput({'class': 'form-contrl'}),
            'description': forms.Textarea({'class': 'form-control'}),
            'rating': forms.NumberInput({'class' : 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }