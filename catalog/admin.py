from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "active")
    list_filter = ("active",)
    search_fields = ("title",)
