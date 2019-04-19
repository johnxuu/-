import requests
from bs4 import BeautifulSoup
import time
def get_movies():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	}
	book_list = []
	for i in range(1,3):
		link = 'http://www.zxcs.me/sort/23/page/'+str(i)
		r = requests.get(link,headers=headers,timeout=25)
		print(str(i),'页面响应状态码：',r.status_code)
		soup=BeautifulSoup(r.text,'lxml')
		div_list = soup.find_all('dl',id ='plist')
		for each in div_list:
			book=each.a['href']
			book_list.append(book)
			#time.sleep(3)
	return book_list
	
movies = get_movies()
#print(movies)
	
count = 0
for i in movies:
	r = requests.get(i)
	soup=BeautifulSoup(r.text,'lxml')
	div_list1= soup.find('div',class_ = 'down_2').a['href']
	b = requests.get(div_list1)
	soup1 = BeautifulSoup(b.text,'lxml')
	down_url = soup1.find('span',class_ = 'downfile').a['href']
	print(down_url)
	a = requests.get(down_url)
	txt = soup.find('div',id='content').h1.text.strip()
	txt = txt.replace('（校对版全本）','')
	name = txt + '.rar'
	count +=1
	with open(name,'wb') as code:
		code.write(a.content)
	print('已下载完成第{}个'.format(count),name)
