from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "password",
            "phone",
            "city",
            "address",
            "is_staff",
        )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
