from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from order.permisions import OrderIsAdminUserOrReadOnly

from .models import Order
from .serializers import OrderSerializer


@extend_schema(description="Order Related Endpoints", tags=["Order"])
class OrderViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [OrderIsAdminUserOrReadOnly]
