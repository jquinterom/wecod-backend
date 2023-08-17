from rest_framework import viewsets
from .serializer import WeaponSerializer, CategorySerializer, CustomWeaponSerializer
from .models import Weapon, Category, CustomWeapon


class WeaponView(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CustomWeaponView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponSerializer
    queryset = CustomWeapon.objects.all()


"""
class AverageRateCustomWeaponView(viewsets.ModelViewSet):
    serializer_class = RateCustomWeaponSerializer
    queryset = RateCustomWeapon.objects.all()
"""
