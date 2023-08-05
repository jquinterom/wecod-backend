from rest_framework import viewsets
from .serializer import WeaponSerializer
from .models import Weapon


class WeaponView(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()
