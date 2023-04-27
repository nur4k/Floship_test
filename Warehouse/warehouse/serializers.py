from rest_framework import serializers

from warehouse.models import Warehouse


class WareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'number', 'title', 'store', 'status')
