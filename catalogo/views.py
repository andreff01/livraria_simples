from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Livro

class LivroListView(ListView):
	model = Livro
	template_name = 'listar.html'
	context_object_name = 'livros'

class LivroDetailView(DetailView):
	model = Livro
	template_name = 'detalhe.html'
	context_object_name = 'livro'

class LivroCreateView(CreateView):
	model = Livro
	fields = ['titulo', 'autor', 'ano_publicacao', 'editora', 'isbn']
	template_name = 'form.html'
	success_url = reverse_lazy('livro-listar')

class LivroUpdateView(UpdateView):
	model = Livro
	fields = ['titulo', 'autor', 'ano_publicacao', 'editora', 'isbn']
	template_name = 'form.html'
	success_url = reverse_lazy('livro-listar')

class LivroDeleteView(DeleteView):
	model = Livro
	template_name = 'confirm_delete.html'
	success_url = reverse_lazy('livro-listar')
