from django.db import models

from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title


class Shop(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to="shop/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")

    amount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=100.00)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Image(BaseModel):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self) -> str:
        return self.image.path
