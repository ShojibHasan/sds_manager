import scrapy

class AgodaSpider(scrapy.Spider):
    name = "agoda"
    allowed_domains = ["agoda.com"]

    def start_requests(self):
        url = f"https://www.agoda.com/search?city=15470"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for hotel in response.css('.PropertyCard'):
            yield {
                'hotel_name': hotel.css('.PropertyCard__HotelName::text').get().strip(),
                'image_url': hotel.css('.PropertyCard__Image::attr(src)').get(),
                'price': hotel.css('.PropertyCard__Price::text').get(),
                'rating': hotel.css('.ReviewScoreBadge__Score::text').get(),
                'booking_url': response.urljoin(hotel.css('a.PropertyCard__Link::attr(href)').get())
            }
