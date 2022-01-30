from rest_framework.routers import SimpleRouter
from .views import CompanyAPIView

router = SimpleRouter()
router.register("", CompanyAPIView, basename='company')

urlpatterns = [

]
urlpatterns += router.urls