from django.contrib import admin
from .models import Order
from django.contrib.admin import SimpleListFilter
# Register your models here.


class OrderFilter(SimpleListFilter):
    title = 'Lọc đơn' # or use _('country') for translated title
    parameter_name = 'Lọc đơn'

    def lookups(self, request, model_admin):
        return (
            (True, ('Đơn đã hoàn thành')),
            (False, ('Đơn chưa hoàn thành')),
        )
        # You can also use hardcoded model name like "Country" instead of
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(is_completed=self.value())
        else:
            return queryset


def make_published(modeladmin, request, queryset):
    queryset.update(is_completed=True)


make_published.short_description = "Hoàn thành đơn hàng"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_completed=False)


make_unpublished.short_description = "Chưa hoàn thành đơn hàng"


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shipping_address', 'phone_number', 'is_completed', )
    list_filter = (OrderFilter,)
    actions = [make_published, make_unpublished]

admin.site.register(Order, OrderAdmin)
