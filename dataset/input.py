# -*- coding: utf8 -*-
import codecs
import pymongo
#import pymysql
from datetime import datetime

mongo_connection = pymongo.MongoClient("localhost",27017)
db = mongo_connection.Health_One
surveyc = db.survey

'''
mysql_connection = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = 'kku2017',
	db = 'afewgoodman',
	charset = 'utf8'
)
'''

def input_data(filename):
    f = codecs.open(filename, "r", "utf-8")
    line = f.readline()

    while line:
    	survey_string = ""
    	s = line.split("\t")

    	for c in s:
    		survey_string += c

    	#####print(survey_string)
    	#####print(datetime.now())
    	
    	# mongo에 저장
    	surveyc.insert({"survey_string":survey_string, "date":datetime.now()})

    	# mysql에 저장
    	#mg_data = surveyc.find_one({"survey_string":survey_string})
    	#####print(str(mg_data["date"]))

    	#cur = mysql_connection.cursor()
    	#cur.execute("insert into survey_data(user_seq, survey_string, mongo_id, date_regis) values ('20','" + survey_string + "','" + str(mg_data["_id"]) +"','" + str(mg_data["date"]) +"')")

    	line = f.readline()
    	
    #mysql_connection.commit()
    #mysql_connection.close()

if __name__=='__main__':
    input_data("./dataset.txt")
