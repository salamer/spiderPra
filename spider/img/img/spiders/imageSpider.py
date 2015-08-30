from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from img.items import ImgItem

class MyImageSpider(BaseSpider):
	name="image_spider"
	alloed_domains=["http://topi.me/"]
	start_urls=[
		"http://topit.me"
	]

	def parse(self,response):
		hxs=HtmlXPathSelector(response)
		imgs=hxs.select("//img/@src").extract()
		item=ImgItem()
		item['image_urls']=imgs
		return item