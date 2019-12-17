# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView  # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('', HomePageView.as_view(), name='home'),
]
# as_view() needs placed if using Class-Based Views
