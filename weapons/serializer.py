from rest_framework import serializers
from .models import (
    Weapon,
    Category,
    CustomWeapon,
    RateCustomWeapon,
    AverageRateCustomWeapon,
    GameMode,
    Accesory
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
    class Meta:
        model = CustomWeapon
        fields = '__all__'


class RateCustomWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCustomWeapon
        fields = '__all__'


class AverageRateCustomWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageRateCustomWeapon
        fields = '__all__'


class GameModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMode
        fields = '__all__'
