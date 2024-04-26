from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "city",
        "address",
        "is_active",
        "is_admin",
    )

    search_fields = ("email", "phone", "city", "address")
