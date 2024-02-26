from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response

from shop import models
from shop import serializers

from shop.permissions import IsShopAdmin, IsProductAdmin, IsCategoryAdmin


class ShopListCreateAPIView(ListCreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ("title",)


class ShopRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer

    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)


class ProductsListCreateAPIView(ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    permission_classes = (permissions.IsAuthenticated, IsProductAdmin)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.SimpleCategorySerializer

    permission_classes = (permissions.IsAuthenticated, IsCategoryAdmin)
