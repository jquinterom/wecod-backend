from django.contrib import admin
from .models import (
    Weapon,
    Category,
    Mozzle,
    Barrel,
    Optic,
    Stock,
    Perk,
    Lazer,
    Underbarrel,
    Ammunition,
    RearGrip,
    CustomWeapon,
    RateCustomWeapon
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Weapon)
admin.site.register(Mozzle)
admin.site.register(Barrel)
admin.site.register(Optic)
admin.site.register(Stock)
admin.site.register(Perk)
admin.site.register(Lazer)
admin.site.register(Underbarrel)
admin.site.register(Ammunition)
admin.site.register(RearGrip)
admin.site.register(CustomWeapon)
admin.site.register(RateCustomWeapon)
