#coding=utf-8
#�������
import os
# name = "С˵����"
# section = "�½�����"
# content = "С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����С˵����"
# s = os.getcwd()
# #os.mkdir("novel")
# os.chdir("novel")
# f = open(name+".txt","w+")
# f.write(name+"\n")

import urllib2
from bs4 import BeautifulSoup as bs
#��ȡ���������ݣ�ʹ��BeautifulSoup
def getcontents(html):
	soup = bs(html,"html.parser")
	print type(soup)
	neirong = soup.find('div', attrs={'class': 'neirong'}).contents
	return neirong

def gethtml(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
	#html = html.decode("utf-8")
	return html
url = "https://www.51shucheng.com/wuxia/bixuejian/1053.html"


f = open("santi.txt","w+")
neirong = getcontents(gethtml(url))
#����Ϊ3��<br>��ǩ����û��
# if len(neirong) == 0:
	# s = neirong[1].getText()
	# f.write(s.encode("GBK","ignore"))
	# print s
	# print type(s)
# else:
	# for nr in neirong:
		# s = nr.string.encode("GBK","ignore")
		# f.write(s.encode("GBK","ignore"))
#����try�������<br>��ǩʱֱ��getText()
for nr in neirong:
	try:
		s = nr.string.encode("GBK","ignore")
		f.write(s)
	except AttributeError:
		s = nr.getText()
		f.write(s.encode("GBK","ignore"))
f.close()






input("asdf")

