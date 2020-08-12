from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import PopularProduct
from .models import News
from .models import NewsCategory
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.

admin.site.site_header = "Панель управления"


class PopularProductAdmin(admin.ModelAdmin):
    """не нужно, удлить потом"""

    list_display = ('product_id', 'product_name', 'created_at')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
admin.site.register(PopularProduct, PopularProductAdmin)


class NewsAdminForm(forms.ModelForm):
    """расширяем админ форму"""

    body = forms.CharField(label='Текст', widget=CKEditorUploadingWidget()) # прикручиваем виджет едитора, вместо чарфилда
    body_text_preview = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':135}))

    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin (admin.ModelAdmin):
    """Модель новостей в админке"""

    list_display = ['id', 'title', 'short_body_text_preview', 'image_tag', 'category', 'author', 'created_at', 'slug']
    list_display_links = ('id', 'title')
    form = NewsAdminForm
    list_filter = ['category']

    #переопределяем метод записи в в БД
    def save_model(self, request, obj, form, change):
        #получаем имя польз. и записываем в бд
        obj.author = request.user
        obj.save()

    fieldsets = (
        (None, {
            'fields': ('title',
                       ('image', 'image_tag'),
                       'body_text_preview',
                       'body',
                       'keywords',
                       'category',
                       'slug',
                       )
        }),
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     'fields': ('registration_required', 'template_name'),
        # }),
    )
    readonly_fields = ('image_tag', 'slug')

@admin.register(NewsCategory)
class NewsAdmin (admin.ModelAdmin):
    """МОдель админ категории"""

    list_display = ['id', 'name']














