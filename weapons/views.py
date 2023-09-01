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
            """
            avg_custom_weapon = RateCustomWeapon.objects.values(
                'customWeapon').annotate(avg_rate=Avg('rate'))
            """
            avg_custom_weapon = RateCustomWeapon.objects.all()
            avg_custom_weapon1 = RateCustomWeapon.objects.values(
                'customWeapon').annotate(Avg('rate'))

            print(avg_custom_weapon1)

            custom_weapon_Data = []
            for custom_weapon in avg_custom_weapon:
                custom_weapon_Data.append({
                    'customWeapon': str(custom_weapon.customWeapon),
                    'rate': custom_weapon.rate,
                })

            serializer_avg = AverageRateCustomWeaponSerializer(
                instance=avg_custom_weapon, many=True)
            response_data = {
                'status': 'success',
                'message': 'data ok',
                'data': custom_weapon_Data
            }
            # print(response_data)
            """
            avg_custom_weapon1 = RateCustomWeapon.objects.all()

            serializer_avg1 = AverageRateCustomWeaponSerializer(
                instance=avg_custom_weapon1, many=True)
            """

            # select AVG(r.rate), r.* from ratecustomweapon r GROUP by r.customWeaponId;

            # print(serializer_avg.data)
            # print(serializer_avg1.data)

        except RateCustomWeapon.DoesNotExist:
            return errorNotFound("Rate for custom weapons does not exists")

        return successResponse("ddd", response_data)
        # return JsonResponse(response_data)


class AccessoryView(viewsets.ModelViewSet):
    serializer_class = AccesorySerializer
    queryset = Accesory.objects.all()


class CustomWeaponAccessoryView(viewsets.ModelViewSet):
    serializer_class = CustomWeaponAccessorySerializer
    queryset = CustomWeaponAccessory.objects.all()
