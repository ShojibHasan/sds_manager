import json
from django.core.management.base import BaseCommand
from hotel_comparison.models import Hotel

class Command(BaseCommand):
    help = "Import hotel data from JSON"

    def handle(self, *args, **kwargs):
        with open("booking_data.json", "r") as file:
            booking_data = json.load(file)

        # with open("agoda_data.json", "r") as file:
        #     agoda_data = json.load(file)

        hotel_dict = {}

        # Process Booking.com data
        for data in booking_data:
            name = data['hotel_name']
            hotel_dict[name] = {
                'name': name,
                'image_url': data['image_url'],
                'price_booking': float(data['price'].replace('BDT', '').replace(',', '').replace('\xa0', '').strip()) if data['price'] else None,
                'rating': float(data['rating']) if data['rating'] and data['rating'].replace('.', '', 1).isdigit() else None,
                'booking_url': data['booking_url']
            }

        # Process Agoda data
        # for data in agoda_data:
        #     name = data['hotel_name']
        #     if name in hotel_dict:
        #         hotel_dict[name]['price_agoda'] = float(data['price'].replace('$', '').strip()) if data['price'] else None
        #         hotel_dict[name]['agoda_url'] = data['booking_url']

        # Save to database
        for hotel_data in hotel_dict.values():
            Hotel.objects.update_or_create(name=hotel_data['name'], defaults=hotel_data)

        self.stdout.write(self.style.SUCCESS("Successfully imported hotel data"))
