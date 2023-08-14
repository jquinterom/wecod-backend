from rest_framework import viewsets
from .serializer import WeaponSerializer, CategorySerializer
from .models import Weapon, Category


class WeaponView(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()