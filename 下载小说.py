import requests
from bs4 import BeautifulSoup
def get_movies():
	headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	'host':'www.zxcs.me'
	}
	link= 'http://www.zxcs.me/download.php?id=11456'
	r = requests.get(link,headers=headers,timeout=20)
	soup= BeautifulSoup(r.text,'lxml')
	div_list = soup.find('span',class_ = 'downfile')
	name = div_list.a.text + '.rar'
	download= div_list.a['href']
	a = requests.get(download)
	print(download)
	with open(name,'wb') as code:
		code.write(a.content)
get_movies()


