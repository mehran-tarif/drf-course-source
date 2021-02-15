from rest_framework import serializers
from blog.models import Article

class ArticleSerialiser(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = "__all__"
		# exclude = ("created", "updated")