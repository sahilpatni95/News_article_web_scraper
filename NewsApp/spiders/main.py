import scrapy

from NewsApp.items import NewsappItem

class ExampleSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/']
    
    def parse(self, response):
        item = NewsappItem()
       
        all_contents = response.css('.content')
        for content in all_contents:
            #Get informations relevant to the news story
            h_title = content.css('.media__link::text').extract()
            h_tag = content.css('a.media__tag::text').extract()
            h_url = content.css('a.media__link::attr(href)').extract()
            url_tag = content.css('a.tag ::attr(href)').extract()

            # store these informations
            item['title'] = h_title
            item['url'] = h_tag
            item['content_tags'] = h_url
            item['content_tags_url'] = url_tag

            yield item


