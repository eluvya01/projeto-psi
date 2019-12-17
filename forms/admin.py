from django.contrib import admin

from .models import Cliente
from .models import Sessoes

admin.site.register(Cliente)
admin.site.register(Sessoes)
