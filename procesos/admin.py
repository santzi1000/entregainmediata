from django.contrib import admin

from procesos.models import Agenda, Nota, Proceso

admin.site.register(Proceso)
admin.site.register(Agenda)
admin.site.register(Nota)