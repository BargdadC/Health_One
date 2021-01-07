import datetime
import requests
import pymongo
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'ko-KR,ko;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
dt = datetime.datetime.now()
connection = pymongo.MongoClient("localhost", 27017)
db = connection.Health_One
collection = db.link

def get_google_search():
    db.keyword.find().sort('_id', pymongo.ASCENDING)
    #print(db.keyword.find().sort('_id', pymongo.ASCENDING))
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

        r = requests.get(googleUrl2, headers=headers, allow_redirects=False)
        html = r.text
        soup = bs(html, 'html.parser')

        titles = soup.select('h3.LC20lb')
        meta_data = soup.select('span.st')
        dives = soup.select('div.r')
        for title, meta,div in zip(titles, meta_data,dives):
            date = dt.strftime("%Y-%m-%d")
            print(title.text)
            print(meta.text)
            print(div.a['href'])
            print(date)
        #print(meta_data)



if __name__ == '__main__':
    get_google_search()
    # rso > div:nth-child(3) > div > div:nth-child(2) > div > div > div.r > a > h3
    # rso > div:nth-child(3) > div > div:nth-child(1) > div > div > div.r > a