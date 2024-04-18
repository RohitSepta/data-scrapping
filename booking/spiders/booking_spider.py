import scrapy
from datetime import datetime, timedelta
# from dataapp.models import ScrapingData
from asgiref.sync import sync_to_async
from booking.items import ScrapingDataItem
from scrapy_splash import SplashRequest

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    start_urls = ['https://www.booking.com/searchresults.en-gb.html?ss=Kensington+High+Street%2C+London&ssne=Karnataka&ssne_untouched=Karnataka&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARnIAQzYAQHoAQH4AQuIAgGoAgO4ArqxzrAGwAIB0gIkNWI5NWNjNWEtMWQ1ZS00YWU4LTlmOTItNzAxN2U0YWI3ZDVk2AIG4AIB&sid=21c743c86afbfb688b8359a328c07926&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=15754&dest_type=landmark&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5e0a32a1c264005c&ac_meta=GhA1ZTBhMzJhMWMyNjQwMDVjIAAoATICZW46HktlbnNpbmd0b24gSGlnaCBTdHJlZXQsIExvbmRvbkAASgBQAA%3D%3D&checkin=2024-04-10&checkout=2024-05-08&group_adults=2&no_rooms=1&group_children=0']

    def parse(self, response):

        # Extract Particular Location all hotel kinks
        all_hotel_links = response.xpath("//div[@data-testid='property-card']//a[@data-testid='title-link']/@href").extract()

        for hotel_link in all_hotel_links:
            next_page_link = hotel_link
            if next_page_link:
                next_page = response.urljoin(next_page_link)
                request = response.follow(next_page, callback=self.parse_hotel_details,cb_kwargs={'hotel_link': hotel_link})
                yield request


    async def parse_hotel_details(self, response, hotel_link):

        hotel_name = response.xpath("//div[@id='hp_hotel_name']//h2/text()").get()
        hotel_exact_address = response.xpath("//span[@data-node_tt_id='location_score_tooltip']/text()").get()
        hotel_ratings= response.xpath("//div[@data-testid='review-score-right-component']/div/text()").get()
        hotel_reviews = response.xpath("//div[@data-testid='review-score-right-component']//div[contains(text(), 'reviews')]/text()").get()

        date = datetime.now()
        start = date
        end = start + timedelta(days=2)
        ranges = []

        for i in range(1,10):
            start = start + timedelta(days = 2*i)
            end = start + timedelta(days=2+i)
            ranges.append((start,end))

        for start,end in ranges:
            start_string = start.strftime("%Y-%m-%d")
            end_string = end.strftime("%Y-%m-%d")
            next_url = hotel_link.split("?")[0]
            checkout_url = f"{next_url}" + f"?checkin={start_string}&checkout={end_string};"
            next_page = response.urljoin(checkout_url)
            request = response.follow(next_page, callback=self.parse_cheapest_room_price,cb_kwargs={'checkout_url': checkout_url})
            yield request

        item = ScrapingDataItem()
        item['hotel_name'] = hotel_name
        item['hotel_exact_address'] = hotel_exact_address.strip()
        item['hotel_headline_rating'] = hotel_ratings
        item['hotel_number_of_reviews'] = hotel_reviews

        # await self.save_item(item)

        yield item

    def parse_cheapest_room_price(self,response,checkout_url):
        item = {}
        item['response.url'] = response.url
        item['checkout_main_url'] = checkout_url
        print(item,"-----------")
        yield item

    @sync_to_async
    def save_item(self, item):
        item.save()


        