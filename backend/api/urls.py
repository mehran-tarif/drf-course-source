from django.urls import path, include
from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"

urlpatterns = [
	path("", ArticleList.as_view(), name="list"),
	path("<slug:slug>", ArticleDetail.as_view(), name="detail"),
	path("users/", UserList.as_view(), name="user-list"),
	path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
]
