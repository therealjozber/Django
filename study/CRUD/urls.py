from django.urls import path
from . import views

urlpatterns = [
    path("crud-product/", views.product_crud, name="crud-product"),
    path("product-details/<int:pk>", views.product_details, name="product-details"),
    path("product-update/<int:pk>", views.update_product, name="product-update"),
    path("product-delete/<int:pk>", views.delete_product, name="product-delete"),
    path("create-product/", views.create_product, name="create-product"),

]
