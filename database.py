#Question 1
'''
import pymysql as pm


con = pm.connect(host='localhost', database='demo', user='smriti')
cursor = con.cursor()
query = 'create table book(bookID int(5) primary key, titleID varchar(10), location int(3), genre double(10,2))'
cursor.execute(query)


#Question 2
import pymysql as pm


con = pm.connect(host='localhost', database='demo', user='smriti')
cursor = con.cursor()
query = "insert into book(bookID, titleID, location, genre)\
values(%s, %s, %s, %s)"
records = [(1, 'abc', 23, 23000),
(2, 'def', 24, 20000),
(3, 'ghi', 50, 100000)]
cursor.executemany(query, records)
con.commit()


#Question 3
import pymysql as pm


con = pm.connect(host='localhost', database='demo', user='smriti')
cursor = con.cursor()
query = "update book set location=location + 5 where bookID = 2"
cursor.execute(query)
con.commit()
'''

