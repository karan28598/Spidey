from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
	name = "justdial"
	allowed_domains = ["justdial.com"]
	start_urls = ["https://www.justdial.com/"]

	custom_settings = {
		'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
    	}

	rules = [Rule(LinkExtractor(allow=(r"/Mumbai/[0-9]+/.+/.+",)), callback="parse_items",follow=True)]

	def parse_items(self, response):
		
		titles = response.selector.xpath('//span[@class="pl"]')
		items = []
		for titles in titles:
			item = JustdialSampleItem()
			item["title"] = titles.xpath("h4/span/a/store-name").extract()
			item["link"] = titles.xpath("a/@href").extract()
			item["phone"] = titles.xpath("p/contact-info").extract()
			item["address"] = titles.xpath("p/address-info tme_adrssec").extract()
			items.append(item)
		return(items)
		print(response.url) 