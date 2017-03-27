'''
Created on 3. 27, 2017
@author: Devin Sangwouk @ PKU

'''
#==================================================python 2=============================================================

#-*- coding: utf-8 -*-
#all the imports

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import
from bs4 import BeautifulSoup
import urllib2


def getData(url) :
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	r = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(url)
	html = response.read()
	response.close()
	return html

def save_txt(res_txt):
	with open('result.txt','wb') as f:
		f.write(res_txt)
		f.close()

def parsing():


	urls = ['https://movie.douban.com/subject/25900945/comments?start=0&limit=20&sort=new_score&status=P']
	res_txt = ""

	for i,url in enumerate(urls):
		print(str(i+1)+"/"+str(len(urls)))
		###### internet error check ########
		try:
			data = getData(url, code = 'utf8')
		except:
			res_txt += "can't_find\n"
			continue
		###### internet error check ########

		#using beautiful soup
		soup = BeautifulSoup(data,'html.parser')

		# find all comments
		divs = soup.find_all('div',{'class':'comment-item'})

		for div in divs:
			# get user title
			user = div.find('span',{'class':'comment-info'}).find('a').getText().strip()
			# get comment uploaded time
			time = div.find('span',{'class':'comment-time'})['title']
			# get comments
			comment = div.find('p').getText().strip()
			# save to res_txt
			res_txt += user +"\t"+time+"\t"+comment+"\n"

		# save to result.txt
		save_txt(res_txt)


def main():
	parsing()
		
if __name__ == "__main__":
    main()
#==================================================python 2=============================================================

