from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()

class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='delivery-crew').exists()

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name__in=['manager', 'delivery-crew']).exists()
