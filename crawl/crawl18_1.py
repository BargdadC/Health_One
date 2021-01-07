import datetime
import requests
import pymongo
from bs4 import BeautifulSoup as bs

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
black_collection=db.blacklist

def get_google_search():
    try:
        for keywordset_doc in db.keyword.find().sort('_id',pymongo.ASCENDING):
            keyword_list = keywordset_doc['keyword_list']
            keyword_title = keywordset_doc['keyword_title']
            keyword_title_id = keywordset_doc['_id']

            googleUrl = f'https://www.google.co.kr/search?q='
            for keyword in keyword_list:
                googleUrl += (keyword + 'or')

            print(googleUrl)
            for pages in range(0.6):
                geturl = (f'{googleUrl}&start={pages}0')
                r = requests.get(geturl, headers=headers, allow_redirects=False)
                html = r.text
                soup = bs(html,'html.parser')

                titles = soup.select('h3.LC20lb')
                meta_data = soup.select('span.st')
                for title, meta in zip(titles, meta_data):
                    try:
                        date = dt.strftime("%Y-%m-%d")
                        link = title.a['href']
                        r2 = requests.get(link)
                        html2 = r2.text
                        soup2 = bs(html2,'html.parser')
                        w = soup2
                        w2= str(w)
                        w3 = w2.count(keyword_title)
                        check = collection.find_one({"url":link})
                        if check == link:
                            continue
                        elif blacklist == link:
                            continue
                        elif check == None:
                            print(title.text)
                            collection.insert({'title': title.text, 'url': link, 'key_score': w3, 'date': date,
                                           'keyword_title_id': keyword_title_id,'hit': 1,
                                           'pheromone': 1.0, 'like': 0,'meta':meta.text})
                    except:
                        print("could not open %s" % title)
                        continue
    except:
        print({'code': 1, 'msg': "error"})
if __name__ == '__main__':
    get_google_search()
