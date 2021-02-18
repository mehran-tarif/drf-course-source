from django.urls import path, include
from .views import ArticleList, ArticleDetail

app_name = "blog"

urlpatterns = [
	path("", ArticleList.as_view(), name="list"),
	path("<int:pk>", ArticleDetail.as_view(), name="detail"),
]
