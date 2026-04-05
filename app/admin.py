from django.contrib import admin

# Register your models here.
from .models import User, Role # Importamos tus modelos [cite: 1019]

# Registramos para que aparezcan en el panel /admin [cite: 1021, 1022]
admin.site.register(User)
admin.site.register(Role)