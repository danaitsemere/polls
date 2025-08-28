from django.urls import path
from .views import list_products
from .views import product_detail
from .views import create_product

urlpatterns=[
   path("products/", list_products, name="list_products"),
   path("products/<int:id>/", product_detail, name="product_details"),
   path("products/create/", create_product, name="create_product"),
]


