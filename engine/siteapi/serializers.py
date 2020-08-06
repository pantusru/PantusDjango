from rest_framework import serializers
from controlcore.models import News
from controlcore.models import NewsCategory

from django.contrib.auth import get_user_model
User = get_user_model()


class NewsCategorySerializer (serializers.ModelSerializer):
    """категории"""

    amount_news = serializers.SerializerMethodField()
    class Meta:
        model = NewsCategory
        fields = ('id', 'name', 'amount_news')
    def get_amount_news(self, obj):
        return obj.category.count()


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class NewsListSerializer (serializers.ModelSerializer):
    """Список новостей"""

    class Meta:
        model = News
        fields = ('id', 'title', 'body_text_preview','image', 'created_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_at'] = [
                                        {"year": instance.created_at.strftime("%Y"),
                                         "month": instance.created_at.strftime("%m"),
                                         "day": instance.created_at.strftime("%d")}
                                        ]
        return representation




class NewsDetailSerializer (serializers.ModelSerializer):
    """Детали новостей"""

    category = NewsCategorySerializer()
    author = UserSerializer()
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_at'] = [
                                        {"year": instance.created_at.strftime("%Y"),
                                         "month": instance.created_at.strftime("%m"),
                                         "day": instance.created_at.strftime("%d")}
                                        ]
        return representation




