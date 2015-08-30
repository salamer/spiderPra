import urllib2
import urllib
import re

class BDTB:
	def __init__(self,baseUrl,seeLZ):
		self.baseURL=baseUrl
		self.seeLZ='?see_lz='+str(seeLZ)

	def getPage(self,pageNum):
		try:
			url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
			request=urllib2.Request(url)
			response=urllib2.urlopen(request)
			print response.read()
			return response
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print u'wrong',e.reason
				return None
	def getTitle(self):
		page=self.getPage(1)
		pattern=re.compile('<h1 class="core_title_txt.*?">(.*?)</h1>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self):
		page=self.getPage(1)
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getContent(self,page):
		pattern=re.compile('<div id="post_contnt_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		for item in items:
			print item

baseURL='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)
bdtb.getContent(1)
