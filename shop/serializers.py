from rest_framework import serializers

from shop.models import Image, Category, Product, Shop


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "description", "parent")


class SimpleShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("id", "title", "description", "image")


class CategorySerializer(serializers.ModelSerializer):
    children = SimpleCategorySerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Category
        fields = ("id", "title", "description", "parent", "children")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "category",
            "amount",
            "price",
            "is_active",
            "shop",
        )


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "id",
            "title",
            "description",
            "image",
            "created_at",
            "updated_at",
        )
