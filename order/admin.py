from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "user",
        "get_product_stock",
        "quantity",
        "get_product_discout",
        "get_product_sell_price",
        "get_total_price",
        "completed",
    )
    search_fields = ("user", "product")
