from django.urls import path, include
from .views import ArticleList

app_name = "api"

urlpatterns = [
	path("", ArticleList.as_view(), name="list"),
]
