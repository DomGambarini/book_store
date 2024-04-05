from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'author',
        'publication_date',
        'number_of_pages',
        'new_arrival',
        'price',
        'category',
        'by_age',
        'isbn',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

