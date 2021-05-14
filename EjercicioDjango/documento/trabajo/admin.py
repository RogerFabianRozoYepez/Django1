from EjercicioDjango.documento.trabajo.models import Tipo_Documento, ciudad, usuario
from django.contrib import admin
from documento.trabajo.models import *

# Register your models here.

admin.site.register(Tipo_Documento)
admin.site.register(usuario)
admin.site.register(ciudad)
