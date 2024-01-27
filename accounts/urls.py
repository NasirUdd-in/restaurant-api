# api/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (UserViewSet, UserProfileViewSet,RestaurantViewSet, MenuViewSet, ItemViewSet,RestaurantUpdateView,RestaurantListView,MenuUpdateView, 
                  OwnerRestaurantListView,OwnerItemUpdateView,CartView, OrderListView, OrderDetailView,)



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)

router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('res/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('restaurants-list/<int:owner_id>/', RestaurantListView.as_view(), name='restaurant-list'),
    path('menus-update/<int:pk>/', MenuUpdateView.as_view(), name='menu-update'),
    path('menus-list/',OwnerRestaurantListView.as_view(), name='owner-menu-list'),
    path('items-list/<int:pk>/', OwnerItemUpdateView.as_view(), name='owner-item-update'),
    path('cart/', CartView.as_view(), name='cart-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
