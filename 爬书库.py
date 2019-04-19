import requests
from bs4 import BeautifulSoup
def get_movies():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	'host':'www.zxcs.me'
	}
	book_list = []
	for i in range(1,2):
	    link = 'http://www.zxcs.me/sort/23/page/'+str(i)
	    r = requests.get(link,headers=headers,timeout=10)
	    #print(str(i),'页面响应状态码：',r.status_code)
	    print(r.text)

	    # soup=BeautifulSoup(r.text,'lxml')
	    # div_list = soup.find_all('dl',id ='plist')
	    # for each in div_list:
	    # 	book=each.a.text.strip()
	    # 	book_list.append(book)
	return book_list
movies = get_movies()
# a=len(movies)	
# print(movies)
# print(a)
