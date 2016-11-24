from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Distrito(models.Model):
    """Something specific learned about a US"""
    distrito = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.distrito

class Concelho(models.Model):
    """Something specific learned about a US"""
    distrito = models.ForeignKey(Distrito)
    concelho = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.concelho

class Freguesia(models.Model):
    """Something specific learned about a US"""
    concelho = models.ForeignKey(Concelho)
    freguesia = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.freguesia

class Tipo(models.Model):
    """Something specific learned about a US"""
    tipo = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.tipo

class Us(models.Model):
    """Something specific learned about a US"""
    tipo =  models.ForeignKey(Tipo)
    freguesia = models.ForeignKey(Freguesia)
    unidade = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.unidade



class Gruposintomas(models.Model):
    """Something specific learned about a US"""
    gruposintomas = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.gruposintomas

class Opcoesintomas(models.Model):
    """Something specific learned about a US"""
    grupo = models.ForeignKey(Gruposintomas)
    opcoes = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.opcoes

class Seleccaosintomas(models.Model):
    """Something specific learned about a US"""
    opcoes = models.ForeignKey(Opcoesintomas)
    seleccao = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.seleccao

class Recomendacoes(models.Model):
    """Something specific learned about a US"""
    seleccao = models.ForeignKey(Seleccaosintomas)
    recomendacoes = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.recomendacoes