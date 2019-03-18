# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Clientes(models.Model):
	"""docstring for Clientes"""
	class Meta:
		verbose_name_plural = "clientes"
	
	cpf = models.CharField(max_length=15, )
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Servicos(models.Model):
	"""docstring for Clientes"""
	class Meta:
		verbose_name_plural = "serviços"
	
	descricao = models.CharField(max_length=200)
	validade = models.IntegerField(default=30)
	entradas =  models.IntegerField(default=10)
	premio = models.TextField()

	def __str__(self):
		return self.descricao

class Empresas(models.Model):
	"""docstring for Empresas"""
	class Meta:
		verbose_name_plural = "empresas"
	
	nome = models.CharField(max_length=200)
	servicos = models.ManyToManyField(Servicos)
	
	def __str__(self):
		return self.nome

class Registros(models.Model):
	"""docstring for Registros"""
	class Meta:
		verbose_name_plural = "registros"
	
	data = models.DateTimeField(default=timezone.now)
	servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.data.strftime('%m/%d/%Y')

class Premios(models.Model):
	"""docstring for Premios"""
	class Meta:
		verbose_name_plural = "premios"
	
	data = models.DateTimeField(default=timezone.now)
	servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	baixado = models.BooleanField(default=False)

	def __str__(self):
		return self.data.strftime('%m/%d/%Y')