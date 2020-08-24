from gettext import ngettext
from string import Template


from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.core.checks import messages
from django.forms import ImageField
from django.urls import path
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField
from .models import *
from .db_api_methods.restruct_media_files import *
from .views import *





class ProductAdminForm (forms.ModelForm):
    category = TreeNodeMultipleChoiceField(queryset=ProductCategory.objects.all(), level_indicator=u'|--')
    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'pantus_id', 'name', 'sku',  'oem_list', 'nomenclature_code', 'active', ]
    form = ProductAdminForm




class ProductCategoryAdminForm (forms.ModelForm):
    #parent = TreeNodeMultipleChoiceField(queryset=ProductCategory.objects.all(), level_indicator=u'|--')
    class Meta:
        model = ProductCategory
        fields = '__all__'


@admin.register(ProductCategory)
class ProductCategoryAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 30
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)
    form = ProductCategoryAdminForm

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    something.short_description = ('Имя категории')



class ApplicabilitiesAdminForm(forms.ModelForm):
    """расширяем админ форму"""
    #parent = TreeNodeMultipleChoiceField(queryset=ProductCategory.objects.all(), level_indicator=u'|--')
    description = forms.CharField(label='Текст', widget=CKEditorUploadingWidget(config_name='default')) # прикручиваем виджет едитора, вместо чарфилда

    class Meta:
        model = ProductApplicabilities
        fields = '__all__'


@admin.register(ProductApplicabilities)
class ApplicabilitiesAdmin (DraggableMPTTAdmin,):
    """Модель применимостей в админке"""
    # change_list_template = "admin/catalog/ProductApplicabilities/change_list.html"
    # list_display = ['name', ]
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)
    form = ApplicabilitiesAdminForm

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    something.short_description = ('Имя категории')

    def save_model(self, request, obj, form, change):
        #if not change:
        """
        При создании нового объекта перекидываем картинки
        в свою структуру, изменяем ссылки на новые
        """
        obj.save()  # нужно сохранить преждевременно, что бы получить ИД, потом ещё раз пересохранить
        new_html = RestructUploadFile().file_move(
            form.cleaned_data['description'],  # тело описания
            f'/product/applicabilities/{obj.id}',  # новая директория начало от root_media
        )
        obj.description = new_html
        super(ApplicabilitiesAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """удаление файлов объекта"""
        RemoveFilesOnObject().delete(f'/product/applicabilities/{obj.id}')
        super(ApplicabilitiesAdmin, self).delete_model(request, obj)

    def delete_selected_tree(self, ApplicabilitiesAdmin, request, queryset):
        """удаление файлов объекТОВ"""
        n = 0
        for obj in queryset:
            RemoveFilesOnObject().delete(f'/product/applicabilities/{obj.id}')
            obj.delete()
            n += 1
        self.message_user(request, ("Successfully deleted %s items.") % n)


class BrandsImagePhotoInline(admin.TabularInline):
    model = BrandsImagesPhoto
    extra = 1


class BrandsImageCertificateInline(admin.TabularInline):
    model = BrandsImageCertificate
    extra = 1



# class ImagePreviewWidget(forms.widgets.FileInput):
#
#     def render(self, name, value, attrs=None, **kwargs):
#         input_html = super().render(name, value, attrs=None, **kwargs)
#         img_html = mark_safe(f'<br><br><img src="{value.url}"/>')
#         return f'{input_html}{img_html}'



class BrandsFormAdmin(forms.ModelForm):
    #image_logo = forms.ImageField(widget=ImagePreviewWidget,)

    # def has_changed(self):  # used for saving data from initial
    #     changed_data = super(BrandsFormAdmin, self).has_changed()
    #     return bool(self.initial or changed_data)
    #
    #     #print('IMG RED')
    #
    # def clean(self):
    #     cleaned_data = super(BrandsFormAdmin, self).clean()
    #     print(cleaned_data)

    class Meta:
        model = Brands
        fields = '__all__'


    # def clean(self):
    #
    #     if self.changed_data:
    #         print('afadfsdfsdfsdfsdfsfsdfs')







@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'city','description','site', 'image_logo')
    #
    # readonly_fields = ('admin_thumbnail',)
    # admin_thumbnail = AdminThumbnail(image_field='img', template='admin/catalog/Brands/thumbnail.html')
    #
    #
    #
    # # readonly_fields = ['headshot_image']
    # #inlines = [BrandsImagePhotoInline, BrandsImageCertificateInline]
    # #form = BrandsFormAdmin
    #
    # # fieldsets = (
    # #     (None, {
    # #         'fields': (
    # #                    'name',
    # #                    'country',
    # #                    'city',
    # #                    'description',
    # #                    'applicabilities',
    # #                    'category',
    # #                    'site',
    # #                     ('image_logo'),
    # #                   )
    # #     }),
    # #     # ('Advanced options', {
    # #     #     'classes': ('collapse',),
    # #     #     'fields': ('registration_required', 'template_name'),
    # #     # }),
    # # )
    # #
    # # def image_view(self, obj):
    # #     return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % obj.image_logo.url)
    # # #



    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_site.admin_view(BrandsView.as_view()))
        ]
        return custom_urls + urls





