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
    category = models.ForeignKey(        Category, null=False, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name
