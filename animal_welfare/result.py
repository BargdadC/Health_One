from bson import json_util
from bson import json_util
from bson import BSON
import sys
import json
import pymongo

#db연결
conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('animal_Welfare')

#argv[1]값을 전화번호로 가져옴
tel = ""
for arg in sys.argv[1]:
	tel += arg

#전화번호의 가장 최근 survey기록을 가져옴
result = db.survey.find_one({"tel":tel},sort=[{'date',  -1}])

#result 값으로 분야별, 전체 점수 산출
if float(result["data"]["poor"])==0:
	poor = 100
elif 0 < float(result["data"]["poor"]) <= 0.5:
	poor = 90
elif 0.5 < float(result["data"]["poor"]) <= 1:
        poor = 90
elif 1 < float(result["data"]["poor"]) <= 2:
        poor = 90
elif 2 < float(result["data"]["poor"]) <= 3:
        poor = 90
elif 3 < float(result["data"]["poor"]) <= 4:
        poor = 90
elif 4 < float(result["data"]["poor"]) <= 5:
        poor = 90
elif 5 < float(result["data"]["poor"]) <= 6:
        poor = 90
elif 6 < float(result["data"]["poor"]) <= 8:
        poor = 90
elif 8 < float(result["data"]["poor"]) <= 10:
        poor = 90
else :
	poor = 0


#survey기록으로 세부 주의사항을 알려줌
for info in db.result_info.find():
	if eval(info['scope_list'][0]):
		print (info["info"])

#출력
print (result, poor)
#print (json.dumps({result:result},default=json_util.default,ensure_ascii=False))
