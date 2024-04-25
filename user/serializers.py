from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "phone",
            "city",
            "address",
        )

    def create(self, validated_data):
        print(validated_data)
        return CustomUser.objects.create_user(**validated_data)
