from django.contrib import admin
from django.apps import apps
from django.http import HttpRequest

from shop.models import Category, Shop, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_change_permission(self, request, obj=None) -> bool:
        if super().has_change_permission(request, obj):
            if request.user.roles.filter(title="category_admin"):
                return True
        return False

    def has_module_permission(self, request) -> bool:
        if super().has_module_permission(request):
            if request.user.roles.filter(title="product_admin"):
                self.readonly_fields = ("id",)
                self.search_fields = (
                    "id",
                    "title",
                    "parent",
                )
                return True
            return False


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title",)

    readonly_fields = ("id",)
    search_fields = ("title",)

    def has_change_permission(self, request, obj=None) -> bool:
        if super().has_change_permission(request, obj):
            if request.user.roles.filter(title="shop_admin"):
                return True
        return False

    def has_module_permission(self, request) -> bool:
        if super().has_module_permission(request):
            if not request.user.roles.filter(title="shop_admin"):
                self.search_fields = []
                return False
            return True


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


class ImageInline(admin.StackedInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "shop", "price")
    inlines = (ImageInline,)

    def has_change_permission(self, request, obj=None) -> bool:
        if super().has_change_permission(request, obj):
            if request.user.roles.filter(title="product_admin"):
                return True
        return False

    def has_module_permission(self, request) -> bool:
        if super().has_module_permission(request):
            if request.user.roles.filter(title="product_admin"):
                self.readonly_fields = ("id",)
                self.autocomplete_fields = ("shop",)
                self.search_fields = ("id", "title", "shop__title")
                self.list_filter = ("shop", "is_active", "price")
                self.sortable_by = (
                    "price",
                    "amount",
                )
                return True
            return False


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
