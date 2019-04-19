import requests
from bs4 import BeautifulSoup
import time
import csv
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
}
for i in range(1,11):
	link = 'http://beijing.anjuke.com/sale/p'+str(i)
	r = requests.get(link,headers= headers)
	print('现在爬取的是第',i,'页')

	soup = BeautifulSoup(r.text,'lxml')
	house_list = soup.find_all('li','list-item')

	for house in house_list:
		name = house.find('div',class_='house-title').a.text.strip()
		price = house.find('span',class_='price-det').text.strip()
		price_area = house.find('span',class_='unit-price').text.strip()
		no_room = house.find('div',class_='details-item').span.text
		area = house.find('div',class_='details-item').contents[3].text
		floor = house.find('div',class_='details-item').contents[5].text
		year = house.find('div',class_='details-item').contents[7].text
		broker = house.find('span',class_='brokername').text
		broker=broker[1:]
		address = house.find('span',class_='comm-address').text.strip()
		address = address.replace('\xa0\xa0\n                ',' ')
		tag_list = house.find_all('span',class_='item-tags')
		tags = [i.text for i in tag_list]
		output_list = [name,price,price_area,no_room,area,floor,year,broker,address,tags]
		with open('beijingfangjia.csv','a+',encoding = 'UTF-8',newline='') as csvfile:
			w = csv.writer(csvfile)
			w.writerow(output_list)
		print(name,price,price_area,no_room,area,floor,year,broker,address,tags)

	time.sleep(10)		

