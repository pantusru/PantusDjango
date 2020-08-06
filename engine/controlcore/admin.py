from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import PopularProduct
from .models import News
from .models import NewsCategory
from django.contrib import messages
from django.utils.translation import ngettext






# Register your models here.

admin.site.site_header = "My admin panel"


#admin.site.register(PopularProduct)



class PopularProductAdmin(admin.ModelAdmin):
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

    body = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    body_text_preview = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':135}))

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin (admin.ModelAdmin):


    list_display = ['id', 'title', 'short_body_text_preview', 'image_tag', 'author', 'created_at', 'slug']
    list_display_links = ('id', 'title')

    form = NewsAdminForm

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
                       #'combined_fields',
                       )
        }),
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     'fields': ('registration_required', 'template_name'),
        # }),
    )
    readonly_fields = ('image_tag', 'slug')



    # def combined_fields(self, obj):
    #     return obj.combined_fields()

@admin.register(NewsCategory)
class NewsAdmin (admin.ModelAdmin):
    list_display = ['id', 'name']














