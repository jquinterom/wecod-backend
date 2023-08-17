from rest_framework import serializers
from .models import Weapon, Category, CustomWeapon, RateCustomWeapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('id', 'name', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CustomWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomWeapon
        fields = '__all__'


class RateCustomWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCustomWeapon
        fields = ('__all__')
