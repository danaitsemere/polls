from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, add_to_cart, cart_detail, remove_from_cart

router= DefaultRouter()
router.register(r"products", ProductViewSet, basename = "products")
urlpatterns = [
    path('', include(router.urls)),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]

