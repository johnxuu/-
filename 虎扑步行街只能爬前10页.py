import requests
from bs4 import BeautifulSoup
import time
import csv
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
}
for i in range(1,20):
	link = 'https://bbs.hupu.com/bxj-'+str(i)
	r = requests.get(link,headers= headers,timeout=20)
	soup = BeautifulSoup(r.text,'lxml')
	house_list = soup.select('form>div>ul>li')
	for li in house_list:
		q = li.find('div',class_ = 'titlelink box').a.text.strip()
		p = li.find('div',class_ = 'author box').a.text.strip()
		e = li.find('div',class_ = 'author box').contents[5].text.strip()
		a = li.find('span',class_ = 'ansour').text.strip()
		r = a.split('/')[0].strip()
		t = a.split('/')[-1].strip()
		y = li.find('div',class_ = 'endreply box').a.text.strip()
		u = li.find('div',class_ = 'endreply box').span.text.strip()
		data_list = [q,p,e,r,t,y,u]
		with open('hupu.csv','a+',newline='',encoding='utf-8-sig') as csvfile:
			w = csv.writer(csvfile)
			w.writerow(data_list)
			print(i,data_list)
			# time.sleep(1)
	
		
	# time.sleep(25)
