#-*- coding: utf-8 -*-

import requests
import time
from lxml import etree

ans = ""
for page in range(0,91,10):
	url = "http://maoyan.com/board/4?offset=" + str(page)
	request_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	html = requests.get(url, headers = request_headers)
	if html.status_code == 200:

		#print('request successfully')
		#print(html.text)
		content = etree.HTML(html.text)

		for item in range(1,11):
			element = content.xpath("//*[@id='app']/div/div/div[1]/dl/dd[" + str(item) + "]/div/div/div[1]/p[1]/a")
			title = element[0].text.strip()
			element = content.xpath("//*[@id='app']/div/div/div[1]/dl/dd[" + str(item) + "]/div/div/div[1]/p[2]")
			actor = element[0].text.strip()
			element = content.xpath("//*[@id='app']/div/div/div[1]/dl/dd[" + str(item) + "]/div/div/div[2]/p/i[1]")
			score = element[0].text.strip()
			element = content.xpath("//*[@id='app']/div/div/div[1]/dl/dd[" + str(item) + "]/div/div/div[2]/p/i[2]")
			score_2 = element[0].text.strip()
			element = content.xpath("//*[@id='app']/div/div/div[1]/dl/dd[" + str(item) + "]/div/div/div[1]/p[3]")
			release_time = element[0].text.strip()

			movie = "《" + title + "》 " + actor + " 评分：" + score + score_2 + " 上映时间、地点：" + release_time
			print(movie)
			ans += movie + "\n"
		time.sleep(3)
	else:
		print('request error, error code: ' + str(html.status_code))

file = open('result.txt', 'wt')
file.write(ans)
file.close()