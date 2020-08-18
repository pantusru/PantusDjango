
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from news.models import News
from news.models import NewsCategory
from catalog.models import ProductCategory


from django.contrib.auth import get_user_model
User = get_user_model()


class NewsCategorySerializer (serializers.ModelSerializer):
    """Сериализатор категории"""

    amount_news = serializers.SerializerMethodField() # кол-во статтей конкретной категории

    class Meta:
        model = NewsCategory
        fields = ('id', 'name', 'amount_news')

    def get_amount_news(self, obj):
        """считать кол-во статей"""
        return obj.category.count()


class UserSerializer (serializers.ModelSerializer):
    """Сериализатор пользователей"""
    class Meta:
        model = User
        fields = ('id', 'username')


class NewsListSerializer (serializers.ModelSerializer):
    """ Сериализатор Список новостей"""

    class Meta:
        model = News
        fields = ('id', 'title', 'body_text_preview','image', 'created_at')

    def to_representation(self, instance):
        """Переопределяем сериализатор вывода
        Разбиваем дату на отдельные ключи Json год, мес., день
        """

        representation = super().to_representation(instance)
        representation['created_at'] = [
                                        {"year": instance.created_at.strftime("%Y"),
                                         "month": instance.created_at.strftime("%m"),
                                         "day": instance.created_at.strftime("%d")}
                                        ]
        return representation


class NewsDetailSerializer (serializers.ModelSerializer):
    """Сериализатор Детали новостей"""

    category = NewsCategorySerializer()
    author = UserSerializer()
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        """Переопределяем сериализатор вывода
        Разбиваем дату на отдельные ключи Json год, мес., день
        """

        representation = super().to_representation(instance)
        representation['created_at'] = [
                                        {"year": instance.created_at.strftime("%Y"),
                                         "month": instance.created_at.strftime("%m"),
                                         "day": instance.created_at.strftime("%d")}
                                        ]
        return representation


# class CategorySerializer(serializers.ModelSerializer):
#     children = RecursiveField(many=True)
#
#     class Meta:
#         model = ProductCategory
#         fields = ('id', 'name', 'code', 'parent', 'children')

# class RecursiveField(serializers.Serializer):
#
#     def to_native(self, value):
#
#         return CategorySerializer(value, context={"parent": self.parent.object, "parent_serializer": self.parent})
#
# class CategorySerializer(serializers.ModelSerializer):
#     children = RecursiveField(many=True, required=False)
#     full_name = SerializerMethodField("get_full_name")
#
#
#     class Meta:
#         model = ProductCategory
#         fields = ('id', 'name', 'full_name', 'children')
#
#     def get_full_name(self, obj):
#         name = obj.name
#
#         if "parent" in self.context:
#             parent = self.context["parent"]
#
#             parent_name = self.context["parent_serializer"].get_full_name(parent)
#
#             name = "%s - %s" % (parent_name, name, )
#
#         return name


# class RecursiveField(serializers.Serializer):
#     """
#     Self-referential field for MPTT.
#     """
#
#     # def to_native(self, value):
#     #     #return CategorySerializer(value, context={"parent": self.parent.object, "parent_serializer": self.parent})
#     #
#     #     serializer = self.parent.parent.__class__(value, context={"parent": self.parent, "parent_serializer": self.parent})
#     #     return serializer.data






class FilterSerializerProductCategory(serializers.ListSerializer):



    def to_representation(self, data):

        #data = ProductCategory.objects.filter(parent=None)
        print(data)
        return super().to_representation(data)


class RecursiveSerializerProductCategory(serializers.Serializer):


    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ProductCategorySerializer(serializers.ModelSerializer):

    children = RecursiveSerializerProductCategory(many=True)

    class Meta:
        #list_serializer_class = FilterSerializerProductCategory
        model = ProductCategory
        fields = ('id', 'name', 'code', 'parent', 'level', 'children')






