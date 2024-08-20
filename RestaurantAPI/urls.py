from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('menu-items', views.MenuItemListCreate.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>', views.MenuItemDetail.as_view(), name='menu-item-detail'),
    path('cart/menu-items', views.CartList.as_view(), name='cart-items'),
    path('cart/menu-items/delete', views.CartDelete.as_view(), name='cart-items-delete'),
    path('orders', views.OrderListCreate.as_view(), name='order-list-create'),
    path('order-details/<int:pk>', views.OrderDetail.as_view(), name='order-list-detail'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
    path('api/groups/manager/users/<int:pk>', views.ManageGroupUsersView.as_view(), name='manage-group-users'),
    path('order-items', views.OrderItemListCreate.as_view(), name='order-item-list-create'),
    path('order-items/<int:pk>', views.OrderItemDetail.as_view(), name='order-item-detail'),
]