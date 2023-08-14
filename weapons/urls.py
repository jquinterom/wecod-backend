from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from weapons import views

# rest router
router = routers.DefaultRouter()
router.register(r'weapons', views.WeaponView, 'weapons')
router.register(r'categories', views.CategoryView, 'categories')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Weapons api"))
]
