from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'date_joined', 'last_login']
        extra_kwargs = {'password': {'write_only': True}}
        
        