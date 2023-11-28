from django import forms
from django.core.exceptions import ValidationError
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

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if rating is not None and rating > 5:
            raise ValidationError("El rating no puede ser mayor a 5.")

        return rating