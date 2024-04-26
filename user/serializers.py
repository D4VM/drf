from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    is_admin = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "phone", "city", "address", "is_admin")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
