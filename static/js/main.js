document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
    setupEventListeners();
});

function updateCartCount() {
    fetch('/api/cart-count/')
        .then(response => response.json())
        .then(data => {
            const cartCountBadge = document.getElementById('cart-count');
            if (cartCountBadge) {
                if (data.count > 0) {
                    cartCountBadge.textContent = data.count;
                    cartCountBadge.style.display = 'inline-block';
                } else {
                    cartCountBadge.style.display = 'none';
                }
            }
        })
        .catch(error => console.log('Error fetching cart count:', error));
}

function setupEventListeners() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add to cart form submission
    const addToCartForms = document.querySelectorAll('form[action*="add"]');
    addToCartForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Allow default form submission
            // Update cart count after adding
            setTimeout(updateCartCount, 500);
        });
    });

    // Quantity input validation
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value < 1) {
                this.value = 1;
            }
        });
    });
}

// Format price to Indian Rupees
function formatPrice(price) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 2
    }).format(price);
}

// Add to cart with AJAX (optional enhancement)
function addToCartAjax(productId, quantity = 1) {
    const formData = new FormData();
    formData.append('product_id', productId);
    formData.append('quantity', quantity);
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    fetch('/cart/add/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Product added to cart!', 'success');
            updateCartCount();
        } else {
            showNotification('Error adding product to cart', 'error');
        }
    })
    .catch(error => {
        console.log('Error:', error);
        showNotification('Error adding product to cart', 'error');
    });
}

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Show notification
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alertDiv);
            bsAlert.close();
        }, 4000);
    }
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img.lazy').forEach(img => {
        imageObserver.observe(img);
    });
}





