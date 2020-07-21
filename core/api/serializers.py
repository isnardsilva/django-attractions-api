from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import TouristSpot
from attractions.api.serializers import AttractionSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from addresses.api.serializers import AddressSerializer

class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    address = AddressSerializer()

    full_description = serializers.SerializerMethodField()
    
    class Meta:
        model = TouristSpot
        fields = ['id', 'name', 'description', 'okay', 'attractions', 'comments', 'reviews', 'address', 'photo', 'full_description']

    def get_full_description(self, obj):
        return '%s - %s ' % (obj.name, obj.description)