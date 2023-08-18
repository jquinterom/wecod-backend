from rest_framework import viewsets
from .serializer import WeaponSerializer, CategorySerializer, CustomWeaponSerializer, RateCustomWeaponSerializer, AverageRateCustomWeaponSerializer
from .models import Weapon, Category, CustomWeapon, RateCustomWeapon
from django.db.models import Avg


class WeaponView(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CustomWeaponView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponSerializer
    queryset = CustomWeapon.objects.all()


class AverageRateCustomWeaponView(viewsets.ModelViewSet):
    serializer_class = AverageRateCustomWeaponSerializer
    queryset = RateCustomWeapon.objects.values(
        'customWeapon').annotate(avg_rate=Avg('rate'))
