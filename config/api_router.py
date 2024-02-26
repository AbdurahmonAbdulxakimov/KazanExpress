from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet
from shop import views as shop_views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    # Shops
    path("shops/", shop_views.ShopListCreateAPIView.as_view(), name="shop_list_create"),
    path(
        "shops/<int:pk>/",
        shop_views.ShopRetrieveUpdateDestroyAPIView.as_view(),
        name="shop_retrieve_update_destrory",
    ),
    # Products
    path(
        "products/",
        shop_views.ProductsListCreateAPIView.as_view(),
        name="product_list_create",
    ),
    path(
        "products/<int:pk>/",
        shop_views.ProductsRetrieveUpdateDestroyAPIView.as_view(),
        name="product_retrieve_update_destrory",
    ),
    # Categories
    path(
        "categories/",
        shop_views.CategoryListCreateAPIView.as_view(),
        name="category_list",
    ),
    path(
        "categories/<int:pk>/",
        shop_views.CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category_retrieve_update_destrory",
    ),
]
urlpatterns += router.urls
