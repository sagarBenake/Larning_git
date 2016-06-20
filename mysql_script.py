#!/usr/bin/python

import MySQLdb

start_time='2016-02-16x 00:00:00'
end_time='2016-02-18 23:59:59'

sum=0
count=[]

sql="SELECT count(*),BLACKLIST_DOUBTFUL from blacklist_logs where DATE_AND_HOUR >= %s AND DATE_AND_HOUR <=%s group by BLACKLIST_DOUBTFUL"

try:
	db = MySQLdb.connect("","","","prod-mysql-db" )	
	cursor = db.cursor()
	
	cursor.execute(sql,(start_time,end_time))
	
	results = cursor.fetchall()
	
	for row in results:
		sum=sum+row[0]
	
	for row in results:
		perc=float(row[0])*100/sum
		print row[1],"\t\t",perc
except:
	print "Error: unable to fecth data"
finally:
	db.close()

