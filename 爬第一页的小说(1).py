import requests
from bs4 import BeautifulSoup
def get_movies():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	}
	book_list = []

	link = 'http://www.zxcs.me/sort/23/page/1'
	r = requests.get(link,headers=headers,timeout=25)
	    #print(str(i),'页面响应状态码：',r.status_code)

	soup=BeautifulSoup(r.text,'lxml')
	div_list = soup.find_all('dl',id ='plist')
	for each in div_list:
	    book=each.a['href']
	    book_list.append(book)
	return book_list
movies = get_movies()
#print(movies)
count = 0
for i in movies:
	a = requests.get(i)
	soup=BeautifulSoup(a.text,'lxml')
	txt = soup.find('div',id='content').h1.text.strip()
	txt = txt.replace('（校对版全本）','')
	name = txt + '.rar'
	count +=1
	print('已下载完成第{}个'.format(count),i,name)
	with open(name,'wb') as code:
		code.write(a.content)
