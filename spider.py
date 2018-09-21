#-*- coding: utf-8 -*-

import requests
import json
import re
import time
from requests.exceptions import RequestException
from lxml import etree

def get_page(url):
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	reponse = requests.get(url, headers=headers)
	if reponse.status_code == 200:
		return reponse.text
	print("reponse failed")
	return None
def analyze(html):
	title_element = context.xpath("//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a")
	actor_element = context.xpath("//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]")
	actor_element = context.xpath("")
	actor_element = context.xpath("")
def main():
	url = "http://maoyan.com/board/4"
	html = get_page(url)
	file = open('result.txt', 'wt')
	file.write(html)
	file.close()
main()