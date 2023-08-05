from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.name
