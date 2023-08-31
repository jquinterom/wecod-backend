from django.urls import path, include
from rest_framework import routers
from weapons import views

# rest router
router = routers.DefaultRouter()
router.register(r'weapons', views.WeaponView, 'weapons')
router.register(r'categories', views.CategoryView, 'categories')
router.register(r'customWeapons', views.CustomWeaponView, 'customWeapons')
router.register(r'customWeaponsAccessory',
                views.CustomWeaponAccessoryView, 'customWeaponsAccessory')
router.register(r'accessories', views.AccessoryView, 'accessories')

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += [path('rateCustomWeaponsAvg/',
                     views.AverageRateCustomWeaponView.as_view(), name='rateCustomWeaponsAvg'),]
