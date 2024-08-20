from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category, MenuItem, Cart, Order, OrderItem
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, UserSerializer, OrderItemSerializer

# Vues pour les items de menu
class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filterset_fields = ['category', 'price']
    ordering_fields = ['price', 'name']
    search_fields = ['name', 'description']


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Vues pour le panier
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDelete(generics.DestroyAPIView):
    queryset = Cart.objects.all()

# Vues pour les commandes
class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['status', 'created_at']
    ordering_fields = ['created_at', 'total_price']
    search_fields = ['customer__name', 'customer__email']

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ManageGroupUsersView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        group = Group.objects.get(name='managers')
        group.user_set.add(user)
        return Response({'status': 'user added to group'}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        group = Group.objects.get(name='managers')
        group.user_set.remove(user)
        return Response({'status': 'user removed from group'}, status=status.HTTP_200_OK)

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return User.objects.get(pk=user_id)
    
class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer