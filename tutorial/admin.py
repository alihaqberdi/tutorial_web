from django.contrib import admin
from .models import Category, Product, Commentary#, ReplayCommentary
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'slug', 'create', 'update', 'is_activated']
    list_filter = ['category', 'author', 'is_activated']
    list_editable = ['is_activated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Commentary)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product','author','create','update', 'is_activated']
    list_editable = ['is_activated']
    list_filter = ['product', 'author', 'is_activated']


# @admin.register(ReplayCommentary)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['comment', 'product','author','create','update', 'is_activated']
#     list_editable = ['is_activated']
#     list_filter = ['product', 'author', 'is_activated']