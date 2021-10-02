#from Catalogo.models import Locacion
from django.contrib import admin
from Catalogo.models import *

# Register your models here.
admin.site.register(Locacion)
admin.site.register(TipoLugar)
admin.site.register(Lugar)