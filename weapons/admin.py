from django.contrib import admin
from .models import (
    Weapon,
    Category,
    CustomWeapon,
    RateCustomWeapon
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Weapon)
admin.site.register(CustomWeapon)
admin.site.register(RateCustomWeapon)
