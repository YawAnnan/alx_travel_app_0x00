import random
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        # Clear existing data to avoid duplicates
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Create sample listings
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description=f"Description for listing {i+1}",
                price_per_night=random.randint(50, 300),
                location=random.choice(["Accra", "Nairobi", "Lagos", "Cape Town", "Kigali"]),
                created_at=timezone.now(),
            )
            listings.append(listing)

        # Create sample bookings
        for listing in listings:
            for _ in range(2):  # two bookings per listing
                Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest {_+1} for {listing.title}",
                    check_in=timezone.now().date(),
                    check_out=(timezone.now() + timezone.timedelta(days=random.randint(2, 7))).date(),
                )

        # Create sample reviews
        for listing in listings:
            for _ in range(2):  # two reviews per listing
                Review.objects.create(
                    listing=listing,
                    reviewer_name=f"Reviewer {_+1} for {listing.title}",
                    rating=random.randint(1, 5),
                    comment="This is a sample review.",
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
