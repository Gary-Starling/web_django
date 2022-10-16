from rest_framework import permissions
#кастомные доступы

class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #readonly
            return True
        
        return bool(request.user and request.user.is_staff) #Если админ

class IsOwnerOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.who_add == request.user