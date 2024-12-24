from django.contrib import admin
from .models import Bouquets, Category, Orders, OrderItem

admin.site.register(Bouquets)
admin.site.register(Category)
admin.site.register(OrderItem)

from django.contrib import admin
from .models import Orders, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['bouquet', 'quantity']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telephone', 'adress', 'total_bouquets', 'total_price_display')
    inlines = [OrderItemInline]

    @admin.display(description='Количество букетов')
    def total_bouquets(self, obj):
        return sum(item.quantity for item in obj.items.all())

    @admin.display(description='Общая стоимость')
    def total_price_display(self, obj):
        return obj.total_price

