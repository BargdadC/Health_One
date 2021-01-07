# 구글 크롤러
# 역할 : mongodb내 keyword 컬렉션의 모든 목록을 가져와 구글에서 검색 후 결과 주소를 link 컬렉션에 넣어줍니다.
# input : db.getCollection('keyword')
# output : db.getCollection('link')
# 다음 작업 : keyword_set.py

import datetime
import requests
import pymongo
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool
from time import sleep

headers = {
    #'Accept-Encoding': 'gzip, deflate, sdch',
    #'Accept-Language': 'ko-KR,ko;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
dt = datetime.datetime.now()

connection = pymongo.MongoClient("localhost", 27017)
db = connection.Health_One
collection = db.link

def get_google_search():
    try:
        for keywordset_doc in db.keyword.find().sort('_id', pymongo.ASCENDING):
            keyword_list = keywordset_doc['keyword_list']
            keyword_title = keywordset_doc['keyword_title']
            keyword_title_id = keywordset_doc['_id']

            print(keyword_list)
            print(keyword_title)
            print(keyword_title_id)

            googleUrl = f'https://www.google.co.kr/search?q='

            for keyword in keyword_list:
                googleUrl += (keyword + 'or')
            googleUrl2 = googleUrl[:-2]

            print(googleUrl2)

            for pages in range(0,6):
                sleep(0.1)
                geturl = (f'{googleUrl2}&start={pages}0')
                print (geturl)
                r = requests.get(geturl, headers=headers, allow_redirects=False)
                html = r.text
                soup = bs(html, 'html.parser')

                titles = soup.select('h3.LC20lb')
                meta_data = soup.select('span.st')
                dives = soup.select('div.r')
                print(html)
                print(titles)
                
                for title, meta,div in zip(titles, meta_data,dives):
                    try:
                        date = dt.strftime("%Y-%m-%d")
                        link = div.a['href']

                        print(title.text)
                        collection.insert({'title':title.text, 'url': link,'date':date,'pheromone':1.0,'like':0,'meta':meta.text,'keyword_title':keyword_title })


                    except:
                        print("could not open %s" % title)
                        continue
    except:
        print("error")


if __name__ == '__main__':
    get_google_search()
    # rso > div:nth-child(3) > div > div:nth-child(2) > div > div > div.r > a > h3
    # rso > div:nth-child(3) > div > div:nth-child(1) > div > div > div.r > a


    #ver2.01
