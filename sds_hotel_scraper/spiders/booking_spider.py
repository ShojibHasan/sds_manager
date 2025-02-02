import scrapy
from datetime import datetime, timedelta

class BookingSpider(scrapy.Spider):
    name = "booking"
    allowed_domains = ["booking.com"]
    
    def start_requests(self):
        city_id = "-1456928"  # Example: London
        checkin_date = (datetime.today() + timedelta(days=10)).strftime('%Y-%m-%d')
        checkout_date = (datetime.today() + timedelta(days=15)).strftime('%Y-%m-%d')

        base_url = "https://www.booking.com/searchresults.html"
        
        # Start from the first page
        start_offset = 0
        max_results = 500  # Set your target number of hotels
        results_per_page = 25  # Booking.com returns 25 hotels per page

        while start_offset < max_results:
            url = f"{base_url}?city={city_id}&checkin={checkin_date}&checkout={checkout_date}&offset={start_offset}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse)

            start_offset += results_per_page  # Move to the next batch

    def parse(self, response):
        for hotel in response.css("div[data-testid='property-card']"):
            yield {
                "hotel_name": hotel.css("div[data-testid='title']::text").get(default="N/A").strip(),
                "image_url": hotel.css("img[data-testid='image']::attr(src)").get(default="N/A"),
                "price": hotel.css("span[data-testid='price-and-discounted-price']::text").get(default="N/A").strip(),
                "rating": hotel.css("div[data-testid='review-score'] span::text").get(default="N/A").strip(),
                "booking_url": response.urljoin(hotel.css("a[data-testid='property-card-link']::attr(href)").get(default=""))
            }
