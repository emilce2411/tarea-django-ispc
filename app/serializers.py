from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    # Serializador anidado para ver la info del rol, no solo el ID
    role = RoleSerializer(read_only=True) 
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'dni', 'birth_date', 'role', 'activo']