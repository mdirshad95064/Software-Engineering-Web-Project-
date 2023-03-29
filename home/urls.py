from django.urls import path
from .views import *

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('category/<slug>', CategoryView.as_view(), name='category'),
   path('detail/<slug>', DetailView.as_view(), name='detail'),
   path('search', SearchView.as_view(), name='search'),
   path('signup', signup, name='signup'),
]