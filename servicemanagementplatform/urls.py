from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from catalog.views import ServiceViewSet
from orders.views import OrderViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("orders", OrderViewSet, basename="order")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
