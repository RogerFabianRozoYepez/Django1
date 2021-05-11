from django.db import models

class Tipo_Documento (models.Model):
    documento = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('NIT', 'Numero de Identificacion Tributaria')
    ]
    documentos = models.CharField(max_length=2 , choices=documento, default='CC' , primary_key=True)

class usuario (models.Model):
    Identidicacion = models.charfiled(max_length=20, primary_key=True )
    Primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    Segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    Primer_apellido = models.CharField(max_length=20, blank=False, null=False)
    Segundo_apellido = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=20, blank=False, null=False)

class ciudad (models.Model):
    Id_Ciudad =  models.CharField(max_length=50, primary_key=True)