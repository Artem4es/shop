from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "bike", "phone", "comment", "order_date")
    search_fields = ("name", "bike", "comment")
    list_filter = ("order_date",)
    empty_value_display = "-пусто-"


admin.site.register(Order, OrderAdmin)
