from rest_framework import serializers
from .models import MenuModel


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = [
            "menu_id", "restaurant", "menu", "description", "price", "currency", 
            "status", "restaurant_url", "created", "updated"
        ]
