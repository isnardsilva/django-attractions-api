from rest_framework.serializers import ModelSerializer
from addresses.models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'line1', 'line2', 'city', 'state', 'country', 'latitude', 'longitude']