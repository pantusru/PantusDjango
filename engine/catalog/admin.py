from gettext import ngettext

from django import forms
from django.contrib import admin
from django.core.checks import messages
from mptt.admin import MPTTModelAdmin
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

from .models import *




# Register your models here.


#
#
# @admin.register(CategoryDepthLevel_2)
# class CategoryItemInlineLvl_2 (admin.TabularInline):
#     """МОдель админ категории"""
#
#     model = CategoryDepthLevel_2
#     fields = ['name']
#
#
#     # list_display = ['id', 'category_id', 'parent_id', 'name', 'code',
#     #                 'depthlevel']
#
# @admin.register(CategoryDepthLevel_3)
# class CategoryAdminLvl_3 (admin.ModelAdmin):
#     """МОдель админ категории"""
#
#     list_display = ['id', 'category_id', 'parent_id', 'name', 'code',
#                     'depthlevel']
#
#
# @admin.register(CategoryDepthLevel_1)
# class CategoryAdminLvl_1 (admin.ModelAdmin):
#     """МОдель админ категории"""
#
#     list_display = ['id', 'category_id', 'parent_id', 'name', 'code',
#                     'depthlevel']
#
#     inlines = [CategoryItemInlineLvl_2]


# class CategoryItemInlineAdmin_lvl_2(admin.TabularInline):
#     model = CategoryDepthLevel_2
#     fields = ['name']
#
#
# @admin.register(CategoryDepthLevel_1)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'category_id', 'parent_id', 'name', 'code', 'depthlevel']
#     inlines = [CategoryItemInlineAdmin_lvl_2,]

#admin.site.register(CategoryItemInlineAdmin_lvl_2, CategoryAdmin)

# class BrandItemInlineAdmin(admin.TabularInline):
#     model = Product
#     #fields = ['id', 'name']
#
#
# @admin.register(Brand)
# class ProductAdmin(admin.ModelAdmin):
#    # list_display = ['id', 'pantus_id', 'active', 'sku', 'name', 'oem_list', 'nomenclature_code']
#     list_display = ['id', 'name']
#     #inlines = [BrandItemInlineAdmin]



class ProductAdminForm (forms.ModelForm):
    category = TreeNodeMultipleChoiceField(queryset=ProductCategory.objects.all(), level_indicator=u'|--')
    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'pantus_id', 'name', 'sku',  'oem_list', 'nomenclature_code', 'active', ]
    form = ProductAdminForm

@admin.register(ProductCategory)
class ProductCategoryAdmin(MPTTModelAdmin, ):
    change_list_template = "admin/catalog/ProductCategory/change_list.html"

    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


    list_display = ['name', 'id', ]


class CategoryAdmin(TreeNodeModelAdmin):

    # set the changelist display mode: 'accordion', 'breadcrumbs' or 'indentation' (default)
    # when changelist results are filtered by a querystring,
    # 'breadcrumbs' mode will be used (to preserve data display integrity)
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    # use TreeNodeForm to automatically exclude invalid parent choices
    form = TreeNodeForm

admin.site.register(CategoryTest, CategoryAdmin)


