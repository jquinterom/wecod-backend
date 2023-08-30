from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.DO_NOTHING)
    img_url = models.URLField(null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class TypeAccessory(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Accesory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type_accessory = models.ForeignKey(
        TypeAccessory, null=True, on_delete=models.DO_NOTHING)
    category_weapon = models.ForeignKey(
        Category, null=True, on_delete=models.DO_NOTHING)

    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class GameMode(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class CustomWeapon(models.Model):
    name = models.CharField(max_length=200, null=False, default="Uknown")
    original_weapon = models.ForeignKey(
        Weapon, null=False, on_delete=models.DO_NOTHING)
    game_mode = models.ForeignKey(
        GameMode, null=True, on_delete=models.DO_NOTHING)
    img_url = models.URLField(null=True)

    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "CustomWeapon"
        verbose_name_plural = "CustomWeapons"


class CustomWeaponAccessory(models.Model):
    customWeapon = models.ForeignKey(
        CustomWeapon, null=True, on_delete=models.CASCADE)
    accesory = models.ForeignKey(
        Accesory, null=True,  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.customWeapon.name


class RateCustomWeapon(models.Model):
    customWeapon = models.ForeignKey(
        CustomWeapon, blank=True, null=True, on_delete=models.DO_NOTHING)
    rate = models.SmallIntegerField(blank=False, default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.customWeapon.name
