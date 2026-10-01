from django.contrib import admin
from .models import Product, Order, OrderItem, UserProfile
from .models import AboutUs, ContactMessage

from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'updated_at')

admin.site.register(AboutUs)
admin.site.register(ContactMessage)





# Product Admin
# ------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'stock_quantity', 'category')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'created_at')
    readonly_fields = ('created_at', 'updated_at')


# ------------------------
# Order Admin
# ------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    search_fields = ('user__username', 'id')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')


# ------------------------
# OrderItem Admin
# ------------------------
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('product__title', 'order__id')


# ------------------------
# UserProfile Admin
# ------------------------
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number', 'address', 'profile_photo')
    search_fields = ('user__username', 'contact_number', 'address')