from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order


class OrderSerializer(ModelSerializer):
    product_options = SerializerMethodField(read_only=True)
    user_info = SerializerMethodField(read_only=True)
    order_info = SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "product",
            "quantity",
            # Info about product, user, order
            "product_options",
            "user_info",
            "order_info",
        )

    def get_product_options(self, obj) -> dict:
        data = {
            "id": obj.product.id,
            "title": obj.product.title,
            "price": obj.product.price,
            "discount": obj.product.discount,
            "sale_price": obj.product.get_sale_price(),
            "stock": obj.product.stock,
            "color": obj.product.color,
            "size": obj.product.size,
        }
        return data

    def get_user_info(self, obj) -> dict:
        data = {
            "id": obj.user.id,
            "email": obj.user.email,
            "phone": obj.user.phone,
            "city": obj.user.city,
            "address": obj.user.address,
        }
        return data

    def get_order_info(self, obj) -> dict:
        data = {
            "price_per_item": obj.product.get_sale_price(),
            "quantity": obj.quantity,
            "total_price": obj.product.get_sale_price() * obj.quantity,
            "status": obj.status,
            "created_at": obj.created_at,
        }
        return data

    # def get_price_per_item(self, obj) -> float:
    #     return obj.product.get_sale_price()

    # def get_total_price(self, obj) -> float:
    #     return obj.product.get_sale_price() * obj.quantity

    # def get_created_at(self, obj) -> str:
    #     return obj.created_at

    # def get_status(self, obj) -> bool:
    #     return obj.status
