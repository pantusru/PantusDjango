

from django.contrib import admin
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

class BrandItemInlineAdmin(admin.TabularInline):
    model = Product
    #fields = ['id', 'name']


@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
   # list_display = ['id', 'pantus_id', 'active', 'sku', 'name', 'oem_list', 'nomenclature_code']
    list_display = ['id', 'name']
    #inlines = [BrandItemInlineAdmin]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_id']




#admin.site.register(Genre, MPTTModelAdmin)




