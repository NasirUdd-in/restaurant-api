# api/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User, UserProfile,Restaurant, Menu, Item,Cart, CartItem, Order, OrderItem
from .serializers import UserSerializer, UserProfileSerializer, RestaurantSerializer, MenuSerializer, ItemSerializer,CartSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve restaurants owned by the specified owner
        owner_id = self.kwargs.get('owner_id')  # Assumes 'owner_id' is passed in the URL
        return Restaurant.objects.filter(owner__id=owner_id)




class MenuUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class OwnerRestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    

    def get_queryset(self):
        owner_id = self.request.query_params.get('owner_id', None)
        if owner_id:
            return Restaurant.objects.filter(owner_id=owner_id)
        else:
            return Restaurant.objects.filter(owner=self.request.user)


class OwnerItemUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [ IsOwnerOrReadOnly]



class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Cart.objects.get_or_create(user=self.request.user)[0]

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)