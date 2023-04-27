from rest_framework import serializers

from store.models import Store


class StoreSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "pin_cod", "title", "status", "warehouse")
