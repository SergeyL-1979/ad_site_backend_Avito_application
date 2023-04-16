from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

# настройка роутов для модели
ad_router = SimpleRouter()
ad_router.register("ads", AdViewSet, basename="ads")
comment_router = SimpleRouter()
comment_router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ad_router.urls)),
    path("", include(comment_router.urls)),
]
