from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
from product.models import Product
from product.serializers import ProductSerializer


@extend_schema(description="Product Related Endpoints", tags=["Product"])
class ProductCreateView(ModelViewSet):
    parser_class = (MultiPartParser,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
