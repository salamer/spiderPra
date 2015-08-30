#import urllib


#url="http://www.lifevc.com"
#html=urllib.urlopen(url)
#content=html.read()
#html.close()

#print content

import urllib
import re

url="http://tieba.baidu.com/p/2336739808"
html=urllib.urlopen(url)
content=html.read()
html.close

img_tag=re.compile(r'class="BDE_Image" src="(.+?\.jpg)"')
img_links=re.findall(img_tag,content)

img_counter=0
for img_link in img_links:
	print img_links,"\n"
	img_name='%s.jpg' % img_counter
	urllib.urlretrieve(img_link,"/home/aljun/pythonlearning/spider/%s" %img_name)
	img_counter+=1