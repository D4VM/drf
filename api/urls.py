from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet
from user.views import CustomUserViewSet
from order.views import OrderViewset

router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"user", CustomUserViewSet)
router.register(r"order", OrderViewset)

urlpatterns = router.urls
