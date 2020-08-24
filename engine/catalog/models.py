from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.template.defaultfilters import truncatechars, register
from django.utils.safestring import mark_safe
from imagekit.models import ImageSpecField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from pilkit.processors import ResizeToFill
from treenode.models import TreeNodeModel
from .db_api_methods.image_review import fit


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
        #return '%s %s %s %s %s' % (self.id, self.name, self.code, self.level, self.parent)
        return self.name






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




class ProductApplicabilities(MPTTModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True, )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children_applicabilities',
                            db_index=True)
    description = RichTextUploadingField(blank=True)

    class Meta:
        ordering = ['-id', 'name']
        verbose_name = 'Применимость'
        verbose_name_plural = 'Применимости'

    def __str__(self):
        return self.name

    @register.filter
    def to_class_name(value):
        return value.__class__.__name__


    # Обрезаем текст превью для админки если больше 100 символов
    def get_description(self):
        return self.description[:500]

    get_description.short_description = "description"

class Brands (models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    applicabilities = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    site =  models.CharField(max_length=255)
    description = models.TextField()
    image_logo = models.ImageField()





    # def image_tag(self):
    #     if self.image_logo:
    #         return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image_logo.url)
    #     else:
    #         return 'No Image Found'
    # image_tag.short_description = 'Изображение'


    img = ImageSpecField(
        source='image_logo',
        processors=[ResizeToFill(160, 160)],
        format='JPEG',
        options={'quality': 85}
    )


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id', 'name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    # def save(self, *args, **kwargs):
    #     super(Brands, self).save(*args, **kwargs)
    #     if self.image_logo:
    #         fit(self.image_logo.path, 100, 100)




class BrandsImagesPhoto(models.Model):
    property = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank=True, related_name='images_photo')
    image = models.ImageField()

    class Meta:

        verbose_name = 'Изображения фото'
        verbose_name_plural = 'Изображения фото'

class BrandsImageCertificate(models.Model):
    property = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank=True, related_name='images_certificate')
    image = models.ImageField()

    class Meta:

        verbose_name = 'Изображение сертификат'
        verbose_name_plural = 'Изображение сертификат'




