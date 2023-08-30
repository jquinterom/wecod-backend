from rest_framework import viewsets, status
from .serializer import (
    WeaponSerializer,
    CategorySerializer,
    CustomWeaponSerializer,
    RateCustomWeaponSerializer,
    AverageRateCustomWeaponSerializer,
    GameModeSerializer,
    AccesorySerializer,
    CustomWeaponAccessorySerializer
)
from .models import (Weapon, Category, CustomWeapon,
                     RateCustomWeapon, GameMode, Accesory,  CustomWeaponAccessory)
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.errorResponse import errorNotFound
from .utils.successResponse import successResponse


class WeaponView(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CustomWeaponView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponSerializer
    queryset = CustomWeapon.objects.all()


class AverageRateCustomWeaponView(APIView):
    def get(self, request):
        try:
            avg_custom_weapon = RateCustomWeapon.objects.values(
                'customWeapon').annotate(avg_rate=Avg('rate'))
            serializer_avg = AverageRateCustomWeaponSerializer(
                instance=avg_custom_weapon, many=True)
        except RateCustomWeapon.DoesNotExist:
            return errorNotFound("Rate for custom weapons does not exists")

        return successResponse("Data found", serializer_avg.data)


class GameModesView(viewsets.ModelViewSet):
    serializer_class = GameModeSerializer
    queryset = GameMode.objects.all()


# Deleting in the future
class customWeaponTwoView(APIView):

    def get(self, request, id):
        try:
            weapon = Weapon.objects.get(pk=id)
        except Weapon.DoesNotExist:
            return errorNotFound("Weapon Does not exists")

        accessories = Accesory.objects.all()
        weapon_serializer = WeaponSerializer(weapon)
        print(weapon_serializer)
        accessories_serializer = AccesorySerializer(accessories, many=True)
        response_data = {"customWeapon": weapon_serializer.data,
                         "accessories": accessories_serializer.data}

        return successResponse("Data found", response_data)


class AccessoryView(viewsets.ModelViewSet):
    serializer_class = AccesorySerializer
    queryset = Accesory.objects.all()


class CustomWeaponAccessoryView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponAccessorySerializer
    queryset = CustomWeaponAccessory.objects.all()
