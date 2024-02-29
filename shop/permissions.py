from rest_framework import permissions


class IsShopAdmin(permissions.BasePermission):
    EDIT_METHODS = (
        "PUT",
        "PATCH",
        "DELETE",
    )

    def has_permission(self, request, view) -> bool:
        print(request.method)

        if request.method in self.EDIT_METHODS:
            if not request.user.roles.filter(title="shop_admin"):
                return False
        return True


class IsProductAdmin(permissions.BasePermission):
    EDIT_METHODS = (
        "PUT",
        "PATCH",
        "DELETE",
    )

    def has_permission(self, request, view) -> bool:
        if request.method in self.EDIT_METHODS:
            if not request.user.roles.filter(title="product_admin"):
                return False
        return True


class IsCategoryAdmin(permissions.BasePermission):
    EDIT_METHODS = (
        "PUT",
        "PATCH",
        "DELETE",
    )

    def has_permission(self, request, view) -> bool:
        if request.method in self.EDIT_METHODS:
            if not request.user.roles.filter(title="category_admin"):
                return False
        return True
