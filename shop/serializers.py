from rest_framework import serializers

from shop.models import Image, Category, Product, Shop


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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image", "product")


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=10000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

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
            "images",
            "uploaded_images",
        )

    def create(self, validated_data):
        uploaded_images = validated_data.pop(
            "uploaded_images",
        )
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            Image.objects.create(image=image, product=product)

        return product


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
