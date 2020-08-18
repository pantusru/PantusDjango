from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from treenode.models import TreeNodeModel


class ProductCategory(MPTTModel):
    """категории продуктов"""

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True,)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.name, self.code, self.level, self.parent)






class Product(models.Model):
    """Продукты"""

    pantus_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    sku = models.CharField(max_length=255)
    oem_list = models.CharField(max_length=255)
    nomenclature_code = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    category = models.ManyToManyField(ProductCategory, related_name="category_related")

    class Meta:
        ordering = ['-id', 'name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name




class CategoryTest(TreeNodeModel):

    # the field used to display the model instance
    # default value 'pk'
    treenode_display_field = 'name'



    name = models.CharField(max_length=50)


    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'