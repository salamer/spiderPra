from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from stack.items import StackItem


class StackSpider(BaseSpider):
	name="stack"
	allowed_domians=['stackoverflow.com']
	start_urls=[
		"http://stackoverflow.com/questions?pagesize=50&sort=newest",
	]
	def parse(self,response):
		questions=HtmlXPathSelector(response).select('//div[@class="summury"]/h3')

		for question in questions:
			item=StackItem()
			title=question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
			url=questionxpath('a[@class="question-hyperlink"]/@href').extract()[0]
			print title,"\n",url,"\n"