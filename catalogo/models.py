
from django.db import models

class Livro(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=100)
	ano_publicacao = models.PositiveIntegerField()
	editora = models.CharField(max_length=100)
	isbn = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return f"{self.titulo} ({self.autor})"
