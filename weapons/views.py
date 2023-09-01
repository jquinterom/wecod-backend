from rest_framework import viewsets, status
from .serializer import (
    WeaponSerializer,
    CategorySerializer,
    CustomWeaponSerializer,
    AverageRateCustomWeaponSerializer,
    AccesorySerializer,
    CustomWeaponAccessorySerializer
)
from .models import (Weapon, Category, CustomWeapon,
                     RateCustomWeapon, Accesory,  CustomWeaponAccessory)
from django.db.models import Avg
from rest_framework.views import APIView
from .utils.errorResponse import errorNotFound
from .utils.successResponse import successResponse
from math import ceil


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
                'customWeapon').annotate(Avg('rate'))

            custom_weapons_avg = []
            for c_weapon_avg in avg_custom_weapon:

                customWeapon = CustomWeapon.objects.get(
                    id=c_weapon_avg['customWeapon'])

                serializer_custom_weapon = CustomWeaponSerializer(
                    customWeapon, many=False)

                custom_weapons_avg.append({
                    'customWeapon': serializer_custom_weapon.data,
                    'avg_rate': ceil(c_weapon_avg['rate__avg'])
                })

            serializer_avg = AverageRateCustomWeaponSerializer(
                custom_weapons_avg, many=False)

        except RateCustomWeapon.DoesNotExist:
            return errorNotFound("Rate for custom weapons does not exists")

        except Exception:
            return errorNotFound("Error to get average by custom weapon")

        return successResponse("Data Found", serializer_avg.instance)


class AccessoryView(viewsets.ModelViewSet):
    serializer_class = AccesorySerializer
    queryset = Accesory.objects.all()


class CustomWeaponAccessoryView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponAccessorySerializer
    queryset = CustomWeaponAccessory.objects.all()
