#!/usr/bin/python3
#coding=utf-8
'''
Created on 3. 27, 2017
@author: Devin Sangwouk @ PKU

'''

#==================================================python 3=============================================================

#==================================================import============================================================
import urllib.parse
import urllib.request
import urllib.error
import http.cookiejar
import codecs
import re
from bs4 import BeautifulSoup
import os
#==================================================set cookie==========================================================
cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
hander = urllib.request.HTTPCookieProcessor(cookie) #HTTPCookieProcessor object to set cookie hander
opener = urllib.request.build_opener(hander) ##set opener by cookie hander
urllib.request.install_opener(opener)


#==================================================get data=============================================================


def getData(url, code) :
	request = urllib.request.Request(url)
	response = opener.open(request)
	text = response.read().decode(code)
	return text

def save_txt(res_txt):
	with open('result.txt','w', encoding="utf8") as f:
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
#==================================================python 3=============================================================

