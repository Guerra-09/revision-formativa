from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Manga
from .forms import MangaForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class MangaListView(ListView):
    model = Manga
    template_name = 'mangas/manga_list.html'
    context_object_name = 'mangas'

@method_decorator(login_required, name='dispatch')
class MangaDetailView(DetailView):
    model = Manga
    template_name = 'mangas/manga_detail.html'
    context_object_name = 'manga'

@method_decorator(login_required, name='dispatch')
class MangaCreateView(CreateView):
    model = Manga
    template_name = 'mangas/mangas_create_form.html'
    form_class = MangaForm
    success_url = reverse_lazy('manga_list')

@method_decorator(login_required, name='dispatch')
class MangaUpdateView(UpdateView):
    model = Manga
    template_name = 'mangas/mangas_create_form.html'
    form_class = MangaForm
    success_url = reverse_lazy('manga_list')

@method_decorator(login_required, name='dispatch')
class MangaDeleteView(DeleteView):
    model = Manga
    template_name = 'mangas/mangas_confirm_delete.html'
    success_url = reverse_lazy('manga_list')