from typing import Any
from django.db import models
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserForm
#Vista generica para crear nuevos usuarios
from django.contrib.auth.forms import UserCreationForm
#Lo traemos para editar widgets
from django import forms

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})

        return form

class ProfileUpdate(UpdateView):
    form_class = UserForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user = self.request.user)
        return profile
    
