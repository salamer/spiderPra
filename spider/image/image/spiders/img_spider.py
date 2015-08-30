import scrapy
from image.items import ImageItem

class ImageSpider(scrapy.Spider):
	name='image_spider'
	allowed_domains=['http://tieba.baidu.com/p/']
	start_urls=[
		"http://tieba.baidu.com/p/3692875903"
	]
	def parse(self,response):

		sel=response.xpath('/html')
		print "the url:"
		print sel.xpath('//img[@class="BDE_Image"]/@src').extract()
		print "\n"
		item=ImageItem()
		item['image_urls']=sel.xpath('//img[@class="BDE_Image"]/@src').extract()
			
			
		return item
