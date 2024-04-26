from django.db import models
from product.models import Product
from user.models import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.product}"

    def get_total_price(self):
        return self.quantity * self.product.get_sale_price()

    def get_product_stock(self):
        return self.product.stock

    def get_product_discout(self):
        return self.product.discount

    def get_product_sell_price(self):
        return self.product.get_sale_price()

    class Meta:
        ordering = ["-created_at"]
