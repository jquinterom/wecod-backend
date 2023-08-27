from django.urls import path, include
from rest_framework import routers
from weapons import views

# rest router
router = routers.DefaultRouter()
router.register(r'weapons', views.WeaponView, 'weapons')
router.register(r'categories', views.CategoryView, 'categories')
router.register(r'customWeapons', views.CustomWeaponView, 'customWeapons')
router.register(r'rateCustomWeapons',
                views.AverageRateCustomWeaponView, 'rateCustomWeapons')
router.register(r'gameModes',
                views.GameModesView, 'gameModes')


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('customWeaponTwo/<int:id>/', views.customWeaponTwoView.as_view(),
         name='customWeaponTwo')
]
