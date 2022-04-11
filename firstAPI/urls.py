from django.urls import path, include
from rest_framework.routers import DefaultRouter
from firstAPI import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cars', views.CarViewSet, basename='cars')
router.register(r'fleets', views.FleetViewSet, basename='fleets')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
