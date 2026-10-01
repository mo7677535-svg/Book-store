from django.db import models
from django.contrib.auth.models import User
from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default='Pustak Hub')
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    # Contact Info
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Social Media
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    # Footer / SEO
    footer_text = models.TextField(blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
# ------------------------
# Product Model
# ------------------------
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100, default='Fiction')
    stock_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


#ABout Us Model
class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    img = models.ImageField(upload_to='about_us/', default='about_us/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Us - {self.created_at.strftime('%Y-%m-%d')}"
    

class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

# ------------------------
# Order Model
# ------------------------
class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    class Meta:
        ordering = ['-created_at']


# ------------------------
# Order Item Model
# ------------------------
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"

    class Meta:
        ordering = ['-created_at']


# ------------------------
# User Profile Model
# ------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')

    def __str__(self):
        return self.user.username