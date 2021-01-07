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
dt = datetime.datetime.now()  # ?œê°„?¤ì •

connection = pymongo.MongoClient("localhost", 27017)
db = connection.Health_One
collection = db.link


# DB?´ìš© ì¶œë ¥?ŒìŠ¤?¸ì‹œ 5~7ë²?28~29ë²?ì£¼ì„ì²˜ë¦¬ ?„ìš”

def get_google_search():
    try:
        for keywordset_doc in db.keyword_set.find().sort('survey_index', pymongo.ASCENDING):
            keyword_list = keywordset_doc['keyword_list']
            keyword_title = keywordset_doc['keyword_title']
            keyword_title_id = keywordset_doc['_id']

            googleUrl = f'https://www.google.co.kr/search?source=hp&q='
            for keyword in keyword_list:
                googleUrl += (keyword + 'OR')
            googleUrl += (keyword)

            for pages in range(0, 6):  # ?¤ìŒ?˜ì´ì§€ë¥??„í•œ forë¬?                geturl = (f'{googleUrl}&start={pages}0')  # ?¬ë¡¤ë§í•  url?¤ì •
                r = requests.get(geturl, headers=headers, allow_redirects=False)  # headerë¥??ìš©???¬ë¡¤ë§?r???€??                html = r.text
                soup = bs(html, 'html.parser')  # 25-26 ?¬ë¡¤ë§?êµ¬ë¬¸

                titles = soup.select('h3.r')  # ì£¼ìš” ê²€??ë¶€ë¶„ì¸ h3, r?œê·¸ ?€??                meta_data = soup.select('span.st')

                print(geturl)
                for title, meta in zip(titles, meta_data):  # ê°?ë¶€ë¶„ë³„ ?¬ë¡¤ë§??˜ë‚˜??ë§í¬ë§ˆë‹¤ ë°˜ë³µ??
                    try:
                        date = dt.strftime("%Y-%m-%d")  # ? ì§œ
                        link = title.a['href']
                        r2 = requests.get(link)
                        html2 = r2.text
                        soup2 = bs(html2, 'html.parser')
                        w = soup2
                        w2 = str(w)  # ?¨ì–´ì¹´ìš´?…ì„ ?„í•œ ë¶€ë¶?                        w3 = w2.count(keyword_title)
                        # collection.findOneAndUpdate({"title":title.text,"url":link2,"key_score":w3,"date":date}, upsert=True)
                        check = collection.find_one({"url": link})
                        print(check)
                        print(title.text)
                        print(link)
                        print(w2.count(keyword_title))
                        print(date)
                        print(meta.text)
                        if check == link:
                            continue
                        elif check == None:
                            collection.insert({'title': title.text, 'url': link, 'key_score': w3, 'date': date,
                                           'keyword_title_id': keyword_title_id,'hit': 1,
                                           'pheromone': 1.0, 'like': 0,'meta':meta.text})

                    except:
                        print("could not open %s" % title)
                        continue

        print({'code': 100, 'msg': "?¬ë¡¤ë§ì´ ?„ë£Œ?˜ì—ˆ?µë‹ˆ??"})

    except:
        print({'code': 1, 'msg': "?¤ë¥˜ê°€ ë°œìƒ?˜ì??µë‹ˆ??"})

def get_word_count(url, query):
    r2 = requests.get(url)
    html2 = r2.text
    soup2 = bs(html2, 'html.parser')
    w = soup2
    w.count(query)

if __name__ == '__main__':
    # for keywordset_doc in db.keyword_set.find().sort('survey_index',pymongo.ASCENDING):
    #   keyword_list = keywordset_doc['keyword_list']
    #  keyword_title = keywordset_doc['keyword_title']
    #pool= Pool(processes=2)
    #pool.map(get_google_search())
    get_google_search()


