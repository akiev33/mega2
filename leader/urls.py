from rest_framework.routers import SimpleRouter
from .views import LeaderAPIView


router = SimpleRouter()
router.register("", LeaderAPIView, basename='leader')


urlpatterns = [

]
urlpatterns += router.urls




