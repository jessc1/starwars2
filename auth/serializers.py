from rest_framework import serializers
from core.serializers import UserSerializer
from core.models import User

class RegisterSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)