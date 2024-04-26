from django.contrib import admin

from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = (
        "title",
        "price",
        "stock",
        "discount",
        "get_sale_price",
        "category",
        "child_category",
        "size",
        "color",
    )
    search_fields = (
        "title",
        "price",
        "stock",
        "discount",
        "category",
        "child_category",
    )
