from rest_framework.routers import SimpleRouter
from .views import Bank_accountAPIView

router = SimpleRouter()
router.register("", Bank_accountAPIView, basename='bank')

urlpatterns = [

]
urlpatterns += router.urls