from django.core.validators import MaxValueValidator
from django.db import models


class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    rz = models.CharField(max_length=8)
    vin = models.CharField(max_length=17)
    power = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    engine_volume = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    signature_code = models.CharField(max_length=10, null=True, blank=True)
    year_of_production = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999)])
    fleet = models.ForeignKey("Fleet", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.brand_name} ({self.rz})"

    @property
    def price_with_vat(self):
        if self.price:
            result_price = self.price * 1.21
            return f"{result_price} CZK"
        else:
            return None


class Fleet(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    default_fleet = models.BooleanField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
