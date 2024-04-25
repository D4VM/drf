from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from .models import CustomUser
from .serializers import CustomUserSerializer


@extend_schema(description="User Related Endpoints", tags=["User"])
class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True, is_admin=False)
    serializer_class = CustomUserSerializer
