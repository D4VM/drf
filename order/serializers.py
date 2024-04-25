from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order


class OrderSerializer(ModelSerializer):
    product_options = SerializerMethodField()
    price_per_item = SerializerMethodField()
    total_price = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "user",
            "product",
            "product_options",
            "quantity",
            "price_per_item",
            "total_price",
            "created_at",
        )

    def get_product_options(self, obj) -> dict:
        data = {
            "id": obj.product.id,
            "name": obj.product.title,
            "price": obj.product.price,
            "sale_price": obj.product.sale_price(),
            "color": obj.product.color,
            "size": obj.product.size,
        }
        return data

    def get_price_per_item(self, obj) -> float:
        return obj.product.price

    def get_total_price(self, obj) -> float:
        return obj.product.sale_price() * obj.quantity

    def get_created_at(self, obj) -> str:
        return obj.created_at
