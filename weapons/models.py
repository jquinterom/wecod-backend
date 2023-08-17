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
        Category, null=True, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Mozzle(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Barrel(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Optic(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Perk(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Lazer(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Underbarrel(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class Ammunition(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class RearGrip(models.Model):
    name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class CustomWeapon(models.Model):
    name = models.CharField(max_length=200, null=False, default="Uknown")
    original_weapon = models.ForeignKey(
        Weapon, null=False, on_delete=models.DO_NOTHING)
    mozzle = models.ForeignKey(
        Mozzle, null=True, on_delete=models.DO_NOTHING)
    barrel = models.ForeignKey(
        Barrel, null=True, on_delete=models.DO_NOTHING)
    optic = models.ForeignKey(Optic, null=True, on_delete=models.DO_NOTHING)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.DO_NOTHING)
    perk = models.ForeignKey(Perk, null=True, on_delete=models.DO_NOTHING)
    lazer = models.ForeignKey(Lazer, null=True, on_delete=models.DO_NOTHING)
    underbarrel = models.ForeignKey(
        Underbarrel, null=True, on_delete=models.DO_NOTHING)
    ammunition = models.ForeignKey(
        Ammunition, null=True, on_delete=models.DO_NOTHING)
    reargrip = models.ForeignKey(
        RearGrip, null=True, blank=True, on_delete=models.DO_NOTHING)

    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name


class RateCustomWeapon(models.Model):
    customWeapon = models.ForeignKey(
        CustomWeapon, blank=True, null=True, on_delete=models.DO_NOTHING)
    rate = models.SmallIntegerField(blank=False, default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.id
