# -*- coding: utf8 -*-
import pymongo
import time


#커넥션 생성
connection = pymongo.MongoClient('localhost', 27017)
db = connection.Health_One

t = (2018, 1, 1, 0, 0, 0, 0, 0, 0)
default_time = time.mktime(t)

def insert_link_data():
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠1",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠2",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠3",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠4",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠5",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠6",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠7",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠8",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })
    db.link.insert_one(
    {
        "title" : "중년 폐암 컨텐츠9",
        "url" : "http://kddlab.kku.ac.kr",
        "date" : "2018-10-12",
        "keyword_title_id" : 'ObjectId("5bc08b6681527052ba6c462d")',
        "keyword_title" : "중년 폐암",
        "category" : "암",
        "hit" : 1,
        "pheromone" : 1.0,
        "like" : 0,
        "meta" : "메타몽"
    })

insert_link_data()
