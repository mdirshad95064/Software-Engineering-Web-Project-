from django.urls import path
from .views import *

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('category/<slug>', CategoryView.as_view(), name='category'),
   path('detail/<slug>', DetailView.as_view(), name='detail'),
   path('search', SearchView.as_view(), name='search'),
   path('signup', signup, name='signup'),
   path('cart', CartView.as_view(), name='cart'),
   path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
   path('delete_cart/<slug>', delete_cart, name='delete_cart'),
   path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
   path('review/<slug>', review, name='review'),
   path('my-account', MyaccountView.as_view(), name='my-account'),
   path('product-list', ProductlistView.as_view(), name='product-list'),
   path('contact', contactus, name='contact'),
   path('checkout', CheckoutView.as_view(), name='checkout'),
   path('wishlist', WishlistView.as_view(), name='wishlist'),
]