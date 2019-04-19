import MySQLdb
conn = MySQLdb.connect(host="localhost",user='root',passwd='root',db='db1')
cur = conn.cursor()
cur.execute("INSERT INTO yonghu(url,content) VALUES('www.baidu.com','百度')")
cur.close()
conn.commit()
conn.close()