from django.contrib import admin

from django.contrib import admin
from KikanoMamarre7APP.models import Usuario
from KikanoMamarre7APP.models import Editorial
from KikanoMamarre7APP.models import Autor
from KikanoMamarre7APP.models import Genero
from KikanoMamarre7APP.models import Libro
from KikanoMamarre7APP.models import Prestamo
from KikanoMamarre7APP.models import Reserva

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Reserva)

