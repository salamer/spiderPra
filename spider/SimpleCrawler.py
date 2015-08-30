import urllib2
import urlparse
import time
import pprint

import BeautifulSoup

inputURL="http://ergoemacs.github.io/ergoemacs-mode/"

resultUrl={inputURL:False}

def processOneUrl(url):
	try:
		html_page=urllib2.urlopen(url)
		soup=BeautifulSoup.BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			fullurl=urlparse.urljoin(url,link.get('href'))
			if fullurl.startswith(inputURL):
				if(fullurl not in resultUrl):
					resultUrl[fullurl]=False
		resultUrl[url]=True
	except:
		resultUrl[url]=True

def moreToCrawl():
	for url,crawled in iter(resultUrl.iteritems()):
		if not crawled:
			print "moreToCrawl found {}".format(url)
			return url
	return False

while True:
	toCrawl=moreToCrawl()
	if not toCrawl:
		break
	processOneUrl(toCrawl)
	time.sleep(2)

pprint.pprint(resultUrl)