from rest_framework.routers import DefaultRouter
from .views import ProductCreateView

router = DefaultRouter()
router.register("", ProductCreateView, basename="product")

urlpatterns = router.urls
