from django.contrib import admin
from .models import Category, Product, Variation
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale_price', 'inventory', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)