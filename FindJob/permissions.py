from rest_framework import permissions

# проверка разрешения на доступ
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # епроверяет является ли пользователь из запроса - пользователем данного объекта
        if obj.user == request.user:
            return True

class IsOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # если запрашиваемый метод является безопасным (например GET)
        if request.method in permissions.SAFE_METHODS:
            return True
        # иначе проверяет является ли пользователь из запроса - пользователем данного объекта
        return obj.user == request.user

class IsOrderNotSaved(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # проверяет что заказ еще не оплачен и пользователь является создателем заказа
        if (obj.status == 'CR') and (obj.user == request.user):
            return True