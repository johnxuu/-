import requests
from bs4 import BeautifulSoup
import time
import gevent
from gevent.queue import Queue,Empty
from gevent import monkey
monkey.patch_all()


headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	}
link_list = []
for i in range(1,2):
	time.sleep(1)
	link = 'http://www.zxcs.me/sort/23/page/'+str(i)
	r = requests.get(link,headers=headers,timeout=25)
	print(str(i),'页面响应状态码：',r.status_code)
	soup=BeautifulSoup(r.text,'lxml')
	div_list = soup.find_all('dl',id ='plist')
	for each in div_list:
		book=each.a['href']
		t = book.split('/')[-1].strip()
		id_url = 'http://www.zxcs.me/download.php?id='+t
		link_list.append(id_url)



start = time.time()
down_list=[]

def crawler(index):
	
	process_id = 'process-'+str(index)
	while not workQueue.empty():
		url = workQueue.get(timeout = 2)
		try:
			r = requests.get(url,timeout = 20)
			soup=BeautifulSoup(r.text,'lxml')
			down_url = soup.find('span',class_ = 'downfile').a['href']
			down_list.append(down_url)
			txt = soup.find('div',class_='content').h2.text.strip()
			txt = txt.replace('（校对版全本）','')
			name = txt + '.rar'
			a = requests.get(down_url)
			with open('E:\\都市娱乐小说集\\xiaoshuo\\%s'% name,'wb') as code:
				code.write(a.content)
			print(process_id,workQueue.qsize(),r.status_code,url,down_url,name)
			return down_list
		except Exception as e:
			print(process_id,workQueue.qsize(),url,'Error:',e)


  
def boss():
	for url in link_list:
		workQueue.put_nowait(url)

if __name__ == '__main__':
	workQueue = Queue(1000)
	gevent.spawn(boss).join()
	jobs = []
	for i in range(16):
		jobs.append(gevent.spawn(crawler,i))
	gevent.joinall(jobs)

	end = time.time()
	print('总时间为：',end-start)
	print(down_list)
	
	




# count = 0
# for i in movies:
# 	down_url_list = []
# 	r = requests.get(i)
# 	soup=BeautifulSoup(r.text,'lxml')
# 	down_url = soup.find('span',class_ = 'downfile').a['href']
# 	print(down_url)
# 	a = requests.get(down_url)
# 	txt = soup.find('div',class_='content').h2.text.strip()
# 	txt = txt.replace('（校对版全本）','')
# 	name = txt + '.rar'
# 	count +=1
# 	down_url_list = down_url_list.append(down_url)
# 	with open(name,'wb') as code:
# 		code.write(a.content)
# 	print('已下载完成第{}个'.format(count),name)
# print(down_url_list)
