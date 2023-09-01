from rest_framework import viewsets, status
from .serializer import (
    WeaponSerializer,
    CategorySerializer,
    CustomWeaponSerializer,
    RateCustomWeaponSerializer,
    AverageRateCustomWeaponSerializer,
    AccesorySerializer,
    CustomWeaponAccessorySerializer
)
from .models import (Weapon, Category, CustomWeapon,
                     RateCustomWeapon, Accesory,  CustomWeaponAccessory)
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.errorResponse import errorNotFound
from .utils.successResponse import successResponse
import json
from django.http import JsonResponse


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
            avg_custom_weapon = RateCustomWeapon.objects.all()
            avg_custom_weapon1 = RateCustomWeapon.objects.values(
                'customWeapon').annotate(Avg('rate'))

            custom_weapons_avg = []
            for c_weapon_avg in avg_custom_weapon1:
                custom_weapons_avg.append({
                    'customWeapon': CustomWeapon.objects.values().get(id=c_weapon_avg['customWeapon']),
                    'rate_avg': c_weapon_avg['rate__avg']
                })

            serializer_avg = AverageRateCustomWeaponSerializer(
                instance=custom_weapons_avg, many=True)

            print(serializer_avg)

        except RateCustomWeapon.DoesNotExist:
            return errorNotFound("Rate for custom weapons does not exists")

        return successResponse("Data Found", custom_weapons_avg)


class AccessoryView(viewsets.ModelViewSet):
    serializer_class = AccesorySerializer
    queryset = Accesory.objects.all()


class CustomWeaponAccessoryView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponAccessorySerializer
    queryset = CustomWeaponAccessory.objects.all()
