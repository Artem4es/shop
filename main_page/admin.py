from django.contrib import admin

from .models import Order, Brand, BikeModel, Article, Review


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "bike", "phone", "comment", "order_date")
    search_fields = ("name", "bike", "comment")
    list_filter = ("order_date",)
    empty_value_display = "-пусто-"


admin.site.register(Order, OrderAdmin)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BikeModel)
class BikeModelAdmin(admin.ModelAdmin):
    list_display = ("brand", "name", "years", "updated_at")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "bike_model", "created_at")
    list_filter = ("bike_model",)
    search_fields = ("author", "text")
