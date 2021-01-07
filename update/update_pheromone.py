# -*- coding: utf8 -*-
import pymongo
import sys
import json

connection = pymongo.MongoClient("localhost",27017)
db = connection.Health_One
linkc = db.link

# 페로몬 업데이트
def update_pheromone(url):
	try:
	    link_data = linkc.find_one({"url":url})

	    linkc.update({"url":url},{"$set":{"like":link_data["like"] + 1}})
	    #linkc.update({"url":url},{"$set":{"hit":link_data["hit"]+2, "like":link_data["like"] + 1}})

	    keyword_title = link_data['keyword_title']

	    link_set_data = linkc.find({"keyword_title":keyword_title})

	    link_set_like = 0
	    #####link_set_hit = 0

	    for data in link_set_data:
	    	link_set_like += data['like']
	    	#####link_set_hit += data['hit']

	    link_set_data = linkc.find({"keyword_title":keyword_title})

	    for data in link_set_data:
	    	if data['url'] == url:
	    		increase_pheromone = (data['like'] / link_set_like)##### + (data['hit'] / link_set_hit)
	    	else:
	    		increase_pheromone = 0

	    	new_pheromone = (1 - 0.05) * data['pheromone'] + increase_pheromone

	    	linkc.update({"url":data['url']},{"$set":{"pheromone":new_pheromone}})

	    print(json.dumps({'code' : 100, 'msg' : "True"},ensure_ascii=False))
	    return (json.dumps({'code' : 100, 'msg' : "True"},ensure_ascii=False))

	except:
		print(json.dumps({'code' : 1, 'msg' : "False", 'url' : url},ensure_ascii=False))
	    #return {'code' : 1, 'msg' : "False", 'url' : url}

if __name__=='__main__':
	#for i in range(10):
		update_pheromone(sys.argv[1])
