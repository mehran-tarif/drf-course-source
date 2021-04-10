from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = "__all__"

	def validate_title(self, value):
		filter_list = ["javascript", "laravel", "PHP"]

		for i in filter_list:
			if i in value:
				raise serializers.ValidationError("Don't use bad world! : {}".format(i))


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"
