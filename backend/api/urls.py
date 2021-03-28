from django.urls import path, include
from .views import UserViewSet, ArticleViewSet
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('', ArticleViewSet)
router.register('users', UserViewSet)

urlpatterns = [
	path("", include(router.urls)),
]