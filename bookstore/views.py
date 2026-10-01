from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from decimal import Decimal
from .models import Product, Order, OrderItem, UserProfile, SiteSettings, AboutUs, ContactMessage
from .forms import RegisterForm, LoginForm, ProfileForm
from django.db.models import Q

# ------------------------
# Home / Products
# ------------------------
def home(request):
    products = Product.objects.all()[:12]
    context = {
        'products': products,
        'page_title': 'Pustak Hub - Online Book Store'
    }
    return render(request, 'bookstore/home.html', context)

def products_list(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    query = request.GET.get('q')  # navbar search input

    if category:
        products = products.filter(category=category)
    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'page_title': 'Products - Pustak Hub'
    }
    return render(request, 'bookstore/products.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'page_title': f'{product.title} - Pustak Hub'
    }
    return render(request, 'bookstore/product_detail.html', context)

# ------------------------
# Cart
# ------------------------
def cart(request):
    cart_items = request.session.get('cart', {})
    cart_products = []
    total_price = Decimal('0.00')

    for product_id, item in cart_items.items():
        try:
            product = Product.objects.get(pk=int(product_id))
            quantity = item.get('quantity', 1)
            # Ensure quantity does not exceed stock
            if quantity > product.stock_quantity:
                quantity = product.stock_quantity
            item_total = product.price * quantity
            total_price += item_total
            cart_products.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'quantity': quantity,
                'image_url': product.image.url,
                'total': item_total
            })
        except Product.DoesNotExist:
            pass

    context = {
        'cart_items': cart_products,
        'total_price': total_price,
        'cart_count': len(cart_products),
        'page_title': 'Shopping Cart - Pustak Hub'
    }
    return render(request, 'bookstore/cart.html', context)

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        try:
            product = Product.objects.get(pk=int(product_id))
            if str(product_id) in cart:
                cart[str(product_id)]['quantity'] += quantity
            else:
                cart[str(product_id)] = {'quantity': quantity}
            # Prevent adding more than stock
            if cart[str(product_id)]['quantity'] > product.stock_quantity:
                cart[str(product_id)]['quantity'] = product.stock_quantity
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, 'Product added to cart!')
        except Product.DoesNotExist:
            messages.error(request, 'Product does not exist!')

        return redirect('cart')
    return redirect('home')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, 'Product removed from cart!')
    return redirect('cart')

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        try:
            product = Product.objects.get(pk=int(product_id))
            if quantity <= 0:
                if str(product_id) in cart:
                    del cart[str(product_id)]
            else:
                if str(product_id) in cart:
                    cart[str(product_id)]['quantity'] = min(quantity, product.stock_quantity)
            request.session['cart'] = cart
            request.session.modified = True
        except Product.DoesNotExist:
            messages.error(request, 'Product does not exist!')

    return redirect('cart')

# ------------------------
# Checkout
# ------------------------
@login_required
def checkout(request):
    cart_items = request.session.get('cart', {})
    if request.method == 'POST':
        if not cart_items:
            messages.warning(request, 'Your cart is empty!')
            return redirect('cart')

        total_price = Decimal('0.00')
        order_items = []

        for product_id, item in cart_items.items():
            try:
                product = Product.objects.get(pk=int(product_id))
                quantity = item.get('quantity', 1)
                if quantity > product.stock_quantity:
                    if product.stock_quantity > 0:
                        messages.warning(request, f"Only {product.stock_quantity} of '{product.title}' available. Added max available to your order.")
                        quantity = product.stock_quantity
                    else:
                        messages.error(request, f"'{product.title}' is out of stock!")
                        continue
                total_price += product.price * quantity
                order_items.append((product, quantity, product.price))
            except Product.DoesNotExist:
                continue

        if not order_items:
            messages.error(request, "No products available to place order!")
            return redirect('cart')

        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='confirmed'
        )
        for product, quantity, price in order_items:
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
            product.stock_quantity -= quantity
            product.save()

        request.session['cart'] = {}
        request.session.modified = True
        messages.success(request, 'Order placed successfully!')
        return redirect('order_detail', pk=order.id)

    # GET request - show checkout page
    cart_products = []
    total_price = Decimal('0.00')
    for product_id, item in cart_items.items():
        try:
            product = Product.objects.get(pk=int(product_id))
            quantity = item.get('quantity', 1)
            if quantity > product.stock_quantity:
                quantity = product.stock_quantity
            item_total = product.price * quantity
            total_price += item_total
            cart_products.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'quantity': quantity,
                'total': item_total,
                'image_url': product.image.url
            })
        except Product.DoesNotExist:
            pass

    context = {
        'cart_items': cart_products,
        'total_price': total_price,
        'page_title': 'Checkout - Pustak Hub'
    }
    return render(request, 'bookstore/checkout.html', context)

# ------------------------
# Profile & Orders
# ------------------------
@login_required
def profile(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=profile)

    orders = Order.objects.filter(user=user)
    context = {
        'user': user,
        'orders': orders,
        'form': form,
        'page_title': 'Profile - Pustak Hub'
    }
    return render(request, 'bookstore/profile.html', context)

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order_items = order.items.all()
    context = {
        'order': order,
        'order_items': order_items,
        'page_title': f'Order #{order.id} - Pustak Hub'
    }
    return render(request, 'bookstore/order_detail.html', context)

# ------------------------
# Authentication
# ------------------------
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'bookstore/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return render(request, 'bookstore/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'bookstore/register.html')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created! Please log in.')
        return redirect('login')

    return render(request, 'bookstore/register.html', {'page_title': 'Register - Pustak Hub'})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'bookstore/login.html', {'page_title': 'Login - Pustak Hub'})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def api_cart_count(request):
    cart = request.session.get('cart', {})
    return JsonResponse({'count': len(cart)})

# ------------------------
# About & Contact Pages
# ------------------------
def about(request):
    about = AboutUs.objects.last()
    return render(request, 'bookstore/about.html', {'about': about, 'page_title': 'About Us - Pustak Hub'})

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')
    return render(request, 'bookstore/contact.html', {'page_title': 'Contact Us - Pustak Hub'})