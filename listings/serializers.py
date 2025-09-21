from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    # show listing details inside a booking
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(),
        source="listing",
        write_only=True
    )

    class Meta:
        model = Booking
        fields = "__all__"
