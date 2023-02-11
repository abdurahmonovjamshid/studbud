from rest_framework.permissions import BasePermission, SAFE_METHODS


class RoomOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(obj.host == request.user or request.user.is_staff)


class MessageOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(obj.user == request.user or request.user.is_staff)
