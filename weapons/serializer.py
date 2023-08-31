from rest_framework import serializers
from .models import (
    Weapon,
    Category,
    CustomWeapon,
    RateCustomWeapon,
    Accesory,
    CustomWeaponAccessory,
)


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class AccesorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CustomWeaponSerializer(serializers.ModelSerializer):
    original_weapon = WeaponSerializer(read_only=True, many=False)

    class Meta:
        model = CustomWeapon
        fields = '__all__'


class RateCustomWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCustomWeapon
        fields = '__all__'


class AverageRateCustomWeaponSerializer(serializers.Serializer):
    customWeapon = CustomWeaponSerializer(read_only=True, many=False)
    avg_rate = serializers.FloatField()


class CustomWeaponAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomWeaponAccessory
        fields = '__all__'
