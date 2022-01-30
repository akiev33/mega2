from rest_framework.routers import SimpleRouter
from .views import SaleAPIView

router = SimpleRouter()
router.register("", SaleAPIView, basename='sale')

urlpatterns = [

]
urlpatterns += router.urls