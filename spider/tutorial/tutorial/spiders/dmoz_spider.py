import scrapy
from tutorial.item import DmozItem

class DmozSpider(scrapy.spiders.Spider):
	name="dmoz"
	allwoed_domains=["dmoz.org"]
	start_urls=[
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
		]

	def parse(self,response):
		for sel in response.xpath("//ul/li"):
			item=DmozItem()
			item["title"]=sel.xpath('a/text()').extract()
			item["link"]=sel.xpath("a/@href").extract()
			item["desc"]=sel.xpath("text()").extract()
			yield item