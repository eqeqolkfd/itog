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

from django.urls import path
from .views import (
    info_view,
    catalog_view,
    add_product_view,
    product_detail_view,
    feedback_view,
    api_view,
    account_view,
    cart_view,
    category_list_view,
    category_products_view,
    add_category_view,
    tag_list_view,
    tag_products_view,
)

urlpatterns = [
    path('', info_view, name='home'),
    path('info/', info_view, name='info'),
    path('catalog/', catalog_view, name='catalog'),
    path('addproduct/', add_product_view, name='addproduct'),
    path('productdetail/', product_detail_view, name='productdetail'),
    path('feedback/', feedback_view, name='feedback'),
    path('api/', api_view, name='api'),
    path('account/', account_view, name='account'),
    path('cart/', cart_view, name='cart'),
    path('categories/', category_list_view, name='category_list'),
    path('categories/add_category/', add_category_view, name='add_category'),
    path('categories/<int:category_id>/', category_products_view, name='category_products'),
    path('tags/', tag_list_view, name='tag_list'),
    path('tags/<int:tag_id>/', tag_products_view, name='tag_products'),
    path('productdetail/<int:pk>/', product_detail_view, name='productdetail'),
]


