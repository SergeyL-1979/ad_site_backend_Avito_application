from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet

# TODO настройка роутов для модели
ad_router = SimpleRouter()
ad_router.register("ads", AdViewSet, basename="ads")

urlpatterns = [
    path("", include(ad_router.urls)),
]
