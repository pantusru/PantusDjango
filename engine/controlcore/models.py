from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from pytils.translit import slugify

class NewsCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.name



# Create your models here.

class PopularProduct(models.Model):
    """Model representing an author."""

    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100, verbose_name="Название")
    product_img = models.CharField(max_length=300)
    product_manufacture = models.CharField(max_length=100)
    product_articul = models.CharField(max_length=100)
    product_oem = models.CharField(max_length=300)
    product_price = models.CharField(max_length=10)
    product_quantity = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['product_id', 'product_name']
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product_name}, {self.product_id}'

class News (models.Model):
    """новости"""

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/', null=True, blank=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Изображение'
    body_text_preview = models.CharField(max_length=200)
    body = RichTextUploadingField(blank=True)
    category = models.ForeignKey('NewsCategory', verbose_name="Категория", on_delete=models.CASCADE, blank=True, null=True, related_name='category')
    keywords = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, editable=False, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    @property
    def short_body_text_preview(self):
        return truncatechars(self.body_text_preview, 200)


    class Meta:
        ordering = ['-id', 'title']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    #создаем слаг только при создании нового объекта
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug

            slugs = News.objects.order_by().values('slug').distinct()
            for currentslug in slugs:
                if formslug == currentslug['slug']:
                    raise forms.ValidationError('Значения Slug должны быть уникальные: такое значение уже существует')
            return formslug


            self.slug = slugify(self.title)




        super(News, self).save(*args, **kwargs)


    def __str__(self):
        return self.title







