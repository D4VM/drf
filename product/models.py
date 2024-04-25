from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=0)
    discount = models.FloatField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)
    child_category = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def sale_price(self) -> float:
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        return self.price

    def __str__(self) -> str:
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self) -> str:
        return f"{self.product.pk} - {self.product.title}"
