from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from .models import Order
from .serializers import OrderSerializer


@extend_schema(description="Order Related Endpoints", tags=["Order"])
class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
