from rest_framework.routers import SimpleRouter
from .views import AddresAPIView

router = SimpleRouter()
router.register("", AddresAPIView, basename='address')

urlpatterns = [

]
urlpatterns += router.urls