"""django_attractions_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import TouristSpotViewSet
from attractions.api.viewsets import AttractionViewSet
from addresses.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from reviews.api.viewsets import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'touristspot', TouristSpotViewSet, basename='TouristSpot')
router.register(r'attractions', AttractionViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
