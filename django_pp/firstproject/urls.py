"""
URL configuration for django_pp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    info_view,
    catalog_view,
    add_product_view,
    product_detail_view,
    cart_view,
    category_list_view,
    category_products_view,
    add_category_view,
    tag_list_view,
    tag_products_view,
    add_to_cart,
    remove_from_cart,
    order_view,
    register_view,
    login_view,
    logout_view,
    delete_category_view,
    edit_category_view,
    edit_product_view,
    delete_product_view,
)

urlpatterns = [
    path('', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('info/', info_view, name='info'),
    path('catalog/', catalog_view, name='catalog'),
    path('addproduct/', add_product_view, name='addproduct'),
    path('productdetail/', product_detail_view, name='productdetail'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('categories/', category_list_view, name='category_list'),
    path('categories/add_category/', add_category_view, name='add_category'),
    path('categories/<int:category_id>/', category_products_view, name='category_products'),
    path('tags/', tag_list_view, name='tag_list'),
    path('tags/<int:tag_id>/', tag_products_view, name='tag_products'),
    path('productdetail/<int:pk>/', product_detail_view, name='productdetail'),
    path('order/', order_view, name='order'),
    path('categories/delete/<int:category_id>/', delete_category_view, name='delete_category'),
    path('categories/edit/<int:category_id>/', edit_category_view, name='edit_category'),
    path('products/<int:pk>/edit/', edit_product_view, name='edit_product'),
    path('products/<int:pk>/delete/', delete_product_view, name='delete_product'),
]


