from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# class CategoryDepthLevel_1(models.Model):
#     category_id = models.IntegerField()
#     parent_id = models.IntegerField()
#     name = models.CharField(max_length=150)
#     code = models.CharField(max_length=150)
#     depthlevel = models.IntegerField()
#
#     class Meta:
#         ordering = ['-id', 'name']
#         verbose_name = 'Категория уровень 1'
#         verbose_name_plural = 'Категории уровень 1'
#
#     def __str__(self):
#         return self.name
#
#
# class CategoryDepthLevel_2(models.Model):
#     category_id = models.IntegerField()
#     parent_id = models.ForeignKey(CategoryDepthLevel_1, verbose_name="parent_id", on_delete=models.CASCADE,
#                                   related_name='category_parent_id_lvl_2')
#     name = models.CharField(max_length=150)
#     code = models.CharField(max_length=150)
#     depthlevel = models.IntegerField()
#
#     class Meta:
#         ordering = ['-id', 'name']
#         verbose_name = 'Категория уровень 2'
#         verbose_name_plural = 'Категории уровень 2'
#
#     def __str__(self):
#         return self.name
#
#
# class CategoryDepthLevel_3(models.Model):
#     category_id = models.IntegerField()
#     parent_id = models.ForeignKey(CategoryDepthLevel_2, verbose_name="parent_id", on_delete=models.CASCADE,
#                                   related_name='category_parent_id_lvl_3')
#     name = models.CharField(max_length=150)
#     code = models.CharField(max_length=150)
#     depthlevel = models.IntegerField()
#
#     class Meta:
#         ordering = ['-id', 'name']
#         verbose_name = 'Категория уровень 3'
#         verbose_name_plural = 'Категории уровень 3'
#
#     def __str__(self):
#         return self.name



# class Brand(models.Model):
#     #id = models.AutoField(primary_key=True, )
#     active = models.BooleanField(default=False)
#     bitrix_id = models.IntegerField()
#     name = models.CharField(max_length=64)
#     code = models.CharField(max_length=64)
#    # test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=True, null=True,)
#
#     class Meta:
#         ordering = ['-id', 'name']
#         verbose_name = 'Брэнд'
#         verbose_name_plural = 'Брэнды'
#
#     def __str__(self):
#         return self.name




# class ProductCategoryRelated(models.Model):
#     category_id = models.ForeignKey()
#     product_id = models.ForeignKey()





class ProductCategory(MPTTModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True,)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_products(self):
        return self.category_products.all()


class Product(models.Model):

    pantus_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    sku = models.CharField(max_length=255)
    oem_list = models.CharField(max_length=255)
    nomenclature_code = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    category = models.ManyToManyField(ProductCategory, related_name="category_products")


    class Meta:
        ordering = ['-id', 'name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name