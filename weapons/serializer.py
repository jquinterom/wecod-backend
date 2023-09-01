from rest_framework import serializers
from .models import (
    Weapon,
    Category,
    CustomWeapon,
    RateCustomWeapon,
    Accesory,
    CustomWeaponAccessory,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class WeaponSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = Weapon
        fields = '__all__'


class AccesorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesory
        fields = '__all__'


class CustomWeaponSerializer(serializers.ModelSerializer):
    original_weapon = WeaponSerializer(read_only=True, many=False)

    class Meta:
        model = CustomWeapon
        fields = '__all__'


class AverageRateCustomWeaponSerializer(CustomWeaponSerializer):
    avg_rate = serializers.FloatField()


class CustomWeaponAccessorySerializer(serializers.ModelSerializer):
    customWeapon = CustomWeaponSerializer(read_only=True, many=False)

    class Meta:
        model = CustomWeaponAccessory
        fields = '__all__'
