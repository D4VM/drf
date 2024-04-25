from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        """
        Create a new product using the validated data provided.

        This method overrides the default `create` method of the serializer to
        create a new `Product` instance and associate it with the images
        provided in the request data.

        Parameters
        ----------
        validated_data : dict
            Dictionary containing the data to create the product.

        Returns
        -------
        Product
            The newly created product instance.
        """
        product = Product.objects.create(**validated_data)
        # Handle image uploads
        request = self.context["request"]
        for image in request.data.getlist("images", []):
            # Validate uploaded file
            if not image.content_type.startswith("image"):
                raise ValidationError("Unsupported file type")

            # Create a new product image instance
            ProductImage.objects.create(product=product, image=image)
        return product
