from rest_framework.routers import SimpleRouter
from .views import First_nameAPIView


router = SimpleRouter()
router.register("", First_nameAPIView, basename='first_name')


urlpatterns = [

]
urlpatterns += router.urls

