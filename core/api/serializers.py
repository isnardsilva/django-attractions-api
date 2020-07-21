from rest_framework.serializers import ModelSerializer
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
    
    class Meta:
        model = TouristSpot
        fields = ['id', 'name', 'description', 'okay', 'attractions', 'comments', 'reviews', 'address', 'photo']