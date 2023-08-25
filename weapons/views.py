from rest_framework import viewsets, status
from .serializer import (
    WeaponSerializer,
    CategorySerializer,
    CustomWeaponSerializer,
    RateCustomWeaponSerializer,
    AverageRateCustomWeaponSerializer,
    GameModeSerializer,
    AccesorySerializer
)
from .models import Weapon, Category, CustomWeapon, RateCustomWeapon, GameMode, Accesory
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


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


class GameModesView(viewsets.ModelViewSet):
    serializer_class = GameModeSerializer
    queryset = GameMode.objects.all()


class customWeaponTwoView(viewsets.ModelViewSet):

    @action(detail=True, methods=["get"])
    def get_queryset(self):
        print(self)
        try:
            weapon = Weapon.objects.get(pk=1)
        except Weapon.DoesNotExist:
            return Respose(
                {"error": "loading weapons"},
                status=status.HTTP_404_NOT_FOUND
            )

        accessories = Accesory.objects.all()

        weapon_serializer = WeaponSerializer(weapon)

        accessories_serializer = AccesorySerializer(accessories, many=True)

        response_data = {"customWeapon": weapon_serializer.data,
                         "accessories": accessories_serializer.data}

        return Response(response_data, status=status.HTTP_200_OK)
