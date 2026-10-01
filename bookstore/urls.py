from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('api/cart-count/', views.api_cart_count, name='api_cart_count'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
