from django.urls import path
from .views import MangaListView, MangaDetailView, MangaCreateView, MangaUpdateView, MangaDeleteView

urlpatterns = [
    path('list/', MangaListView.as_view(), name='manga_list'),
    path('detail/<int:pk>/', MangaDetailView.as_view(), name='manga_list_detail'),
    path('create/', MangaCreateView.as_view(), name='manga_list_create'),
    path('update/<int:pk>/', MangaUpdateView.as_view(), name='manga_list_update'),
    path('delete/<int:pk>/', MangaDeleteView.as_view(), name='manga_list_delete'),
]