from rest_framework import serializers

from catalog.models import Service

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.filter(active=True),
    )

    class Meta:
        model = Order
        fields = ["id", "user", "service", "status", "created_at"]
        read_only_fields = ["id", "user", "status", "created_at"]
