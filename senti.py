# -*- coding: utf-8 -*-
# !/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("localhost","root","3","SentiWordNetNep" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

# होइन

sent = "He is not a bad boy"

rate = 0

for i in sent.split():
	sql_eng_senti = "SELECT * FROM `eng_senti` WHERE SynsetTerms = '%s'" % (i)
	if cursor.execute(sql_eng_senti) != 0:
		data_nep = cursor.fetchall()
		for row in data_nep:
			print "word= ", row[4], row[0],"+ve=", row[2], "-ve=", row[3]
	# print rate
	# print data_nep

db.close()


# राम राम्रो मान्छे हो