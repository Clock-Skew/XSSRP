import scrapy

class XSSSpider(scrapy.Spider):
    name = "xss_spider"

    def __init__(self, domain):
        self.start_urls = [f'http://{domain}']

    def parse(self, response):
        # Identify forms
        for form in response.css('form'):
            yield {
                'url': response.url,
                'form': form.extract()
            }
        # Follow links to next page
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
