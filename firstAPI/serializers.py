from rest_framework import serializers

from firstAPI.models import Car, Fleet


# class CarSerializer(serializers.ModelSerializer):
#     fleet_id = serializers.PrimaryKeyRelatedField(source='fleet', queryset=Fleet.objects.all())  # zobrazí navázaný model jako id
#     # price_vat = serializers.SerializerMethodField()
#     price_vat_with_property = serializers.CharField(source="price_with_vat")
#
#     class Meta:
#         model = Car
#         fields = ("brand_name", "rz", "vin", "power", "price", "price_vat_with_property", "fleet_id")
#
#     # def get_price_vat(self, obj):
#     #     if obj.price:
#     #         result_price = obj.price * 1.21
#     #         return f"{result_price} CZK"
#     #     else:
#     #         return None

class CarListSerializer(serializers.ModelSerializer):
    fleet_id = serializers.PrimaryKeyRelatedField(source='fleet', queryset=Fleet.objects.all())  # zobrazení PK provázaného pole
    # pod novým názvem
    price_vat_with_property = serializers.CharField(source="price_with_vat", read_only=True)  # přidání pole mimo databází
    # read_only = pole jen pro get

    class Meta:
        model = Car
        fields = ("id", "brand_name", "rz", "vin", "power", "price", "price_vat_with_property", "fleet_id")


class CarDetailSerializer(serializers.ModelSerializer):
    fleet_id = serializers.PrimaryKeyRelatedField(source='fleet', queryset=Fleet.objects.all())
    price_vat_with_property = serializers.CharField(source="price_with_vat", read_only=True)

    class Meta:
        model = Car
        fields = ("id", "brand_name", "rz", "vin", "power", "price", "price_vat_with_property", "engine_volume",
                  "year_of_production", "description", "signature_code", "fleet_id")


class FleetSerializer(serializers.ModelSerializer):
    cars = CarListSerializer(source="car_set", many=True)  # zobrazí auta flotily jako list

    class Meta:
        model = Fleet
        fields = ("id", "name", "code", "default_fleet", "date", "cars")
