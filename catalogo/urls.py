from django.urls import path
from .views import LivroListView, LivroDetailView, LivroCreateView, LivroUpdateView, LivroDeleteView

urlpatterns = [
    path('', LivroListView.as_view(), name='livro-listar'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detalhe'),
    path('livro/novo/', LivroCreateView.as_view(), name='livro-criar'),
    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='livro-editar'),
    path('livro/<int:pk>/excluir/', LivroDeleteView.as_view(), name='livro-excluir'),
]
