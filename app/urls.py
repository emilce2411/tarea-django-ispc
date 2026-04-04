from django.urls import path
from .views import UserView, RoleView

urlpatterns = [
    path('users', UserView.as_view()), # Ruta para usuarios [cite: 1244]
    path('roles', RoleView.as_view()), # Ruta para roles [cite: 1245]
]