# -*- coding: utf8 -*-
import pymongo
import time


#커넥션 생성
connection = pymongo.MongoClient('localhost', 27017)
db = connection.Health_One

t = (2018, 1, 1, 0, 0, 0, 0, 0, 0)
default_time = time.mktime(t)

def insert_keyword_data():

    db.keyword.insert_one(
    {
        u'category' : u'암',
        u'survey_index' : ['6<=19700000', '48==1'],
        u'keyword_title' : u'중년 폐암',
        u'keyword_list' : [u'중년 폐암의', u'중년 폐암에', u'중년 암 식단'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'survey_index' : ['23==1', '65==1'],
        u'keyword_title' : u'안구건조증 흡연',
        u'keyword_list' : [u'안구건조증 흡연', u'흡연 눈건강'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'흡연',
        u'survey_index' : ['5==1', '65==1'],
        u'keyword_title' : u'남성 흡연',
        u'keyword_list' : [u'남성 흡연', u'흡연 정자', u'흡연 발기부전'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'흡연',
        u'survey_index' : ['6<=19700000', '29==1'],
        u'keyword_title' : u'중년 이명',
        u'keyword_list' : [u'중년 이명'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'survey_index' : ['5==1', '38==1', '65==1', '59>=4', '60>1000'],
        u'keyword_title' : u'남성 탈모 흡연 음주',
        u'keyword_list' : [u'남성탈모 흡연', u'남성탈모 음주'],
        u'last_update' : default_time
    })

insert_keyword_data()
