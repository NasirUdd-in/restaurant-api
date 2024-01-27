# api/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet,RestaurantViewSet, MenuViewSet, ItemViewSet,RestaurantUpdateView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)

router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('res/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-update'),
]
