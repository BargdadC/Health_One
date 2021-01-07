# contents.py
# 웹에 뿌려질 추천 크롤링 정보를 모아 보내줌

# -*- coding: utf8 -*-
import sys
import json
import base64
import pymongo
from operator import eq
from bson import ObjectId

#커넥션 생성
connection = pymongo.MongoClient('localhost', 27017)
db = connection.Health_One




#웹 서버와 통신을 위한 한글 인코딩
def base64_encoding(value):
    value_bytes = value.encode()
    value_base64 = base64.b64encode(value_bytes)
    value_encoded = str(value_base64)[2:-1]

    return value_encoded


#scope 필드값을 인덱스, 비교연산자, 피연산자로 나누어 dict자료형으로 반환
def convert_to_dict(scope):
    operators = ['=', '<', '>', '==', '<=', '=<', '>=', '=>']
    oprt_idx = len(scope)
    oprt_len = 0

    for operator in operators:
        idx = scope.find(operator)
        if (idx != -1) and (idx <= oprt_idx) and (oprt_len < len(operator)) :
            oprt_idx = idx
            oprt_len = len(operator)

    oprt_start = oprt_idx
    oprt_end = oprt_idx + oprt_len

    operand = scope[oprt_end:]
    if operand == "TRUE" or operand == "True" or operand == "true":
        operand = True;
        # print("true0")
    elif operand == "FALSE" or operand == "False" or operand == "false":
        operand = False;
        # print("false0")

    return {'sur_key':scope[:oprt_start], 'operator':scope[oprt_start:oprt_end], 'operand':operand}

#pagerank 컬렉션을 순회하며 복수조건에 맞는 링크들의 정보를 추출
def contents(survey_id="5c66f3e38d341ffe76142f65"): # sur_str 를 survey_id 로 객체로 변경
    link_list = [] #return될 링크들의 정보를 저장할 리스트
    knowledge_list = [] #return될 링크들의 정보를 저장할 리스트
    video_list = [] #return될 링크들의 정보를 저장할 리스트


    survey_data = db.survey.find_one({"_id":ObjectId(survey_id)})
    # print(survey_data['survey_data'])
    try:
        #각 도큐먼트를 한개씩 조회
        for pagerank_doc in db.pagerank.find():
            flag = True;

            # 문진결과와 복수조건 비교
            for scope_value in pagerank_doc['scope_list']:
                scope = convert_to_dict(scope_value)
                # print(scope)
                operator = str(scope['operator'])
                operand = scope['operand']
                sur_key = scope['sur_key']

                if sur_key in survey_data['survey_data'] :
                    sur_value = survey_data["survey_data"][sur_key]
                    # print("sur_value : " + str(sur_value))
                    # print("operand : " + str(operand))
                    # print("sur_key : " + str(sur_key))
                    #DB에 저장된 조건이 '=' 혹은 '==' 일 때
                    if eq(operator, '=') or eq(operator, '=='):
                        if not float(sur_value) == float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<'일 때
                    elif eq(operator, '<'):
                        if not float(sur_value) < float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>'일 때
                    elif eq(operator, '>'):
                        if not float(sur_value) > float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<=' 혹은 '=<'일 때
                    elif eq(operator, '<=') or eq(operator, '=<'):
                        if not float(sur_value) <= float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>=' 혹은 '=>'일 때
                    elif eq(operator, '>=') or eq(operator, '=>'):
                        if not float(sur_value) >= float(operand):
                            flag = False;
                            break;
                else : 
                    flag = False;

            #모든 복수조건을 만족하면 링크 정보를 dict형으로 link_list에 추가
            if flag:
                link_dict = {}
                link_dict['id'] = str(pagerank_doc['_id'])
                # link_dict['category'] = base64_encoding(pagerank_doc['category'])
                # link_dict['keyword_title'] = base64_encoding(pagerank_doc['keyword_title'])
                link_dict['category'] = base64_encoding(pagerank_doc['category'])
                link_dict['keyword_title'] = base64_encoding(pagerank_doc['keyword_title'])
                link_dict['scope_list'] = pagerank_doc['scope_list']

                link_lists = ['new1_id','new2_id','top1_id','top2_id','top3_id','top4_id','top5_id','ran1_id','ran2_id']
                for link_object in link_lists:
                    if link_object in pagerank_doc :
                        link_dict[link_object] = str(pagerank_doc[link_object])

                link_list.append(link_dict)



        # 지식 베이스 시작
        #각 도큐먼트를 한개씩 조회
        for knowledgerank_doc in db.knowledgerank.find():
            flag = True;

            # 문진결과와 복수조건 비교
            for scope_value in knowledgerank_doc['scope_list']:
                scope = convert_to_dict(scope_value)
                # print(scope)
                operator = str(scope['operator'])
                operand = scope['operand']
                sur_key = scope['sur_key']

                if sur_key in survey_data['survey_data'] :
                    sur_value = survey_data["survey_data"][sur_key]
                    # print("sur_value : " + str(sur_value))
                    # print("operand : " + str(operand))
                    # print("sur_key : " + str(sur_key))
                    #DB에 저장된 조건이 '=' 혹은 '==' 일 때
                    if eq(operator, '=') or eq(operator, '=='):
                        if not float(sur_value) == float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<'일 때
                    elif eq(operator, '<'):
                        if not float(sur_value) < float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>'일 때
                    elif eq(operator, '>'):
                        if not float(sur_value) > float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<=' 혹은 '=<'일 때
                    elif eq(operator, '<=') or eq(operator, '=<'):
                        if not float(sur_value) <= float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>=' 혹은 '=>'일 때
                    elif eq(operator, '>=') or eq(operator, '=>'):
                        if not float(sur_value) >= float(operand):
                            flag = False;
                            break;
                else : 
                    flag = False;

            #모든 복수조건을 만족하면 링크 정보를 dict형으로 knowledge_list에 추가
            if flag:
                knowledge_dict = {}
                knowledge_dict['id'] = str(knowledgerank_doc['_id'])
                # knowledge_dict['category'] = base64_encoding(knowledge_doc['category'])
                # knowledge_dict['keyword_title'] = base64_encoding(knowledge_doc['keyword_title'])
                knowledge_dict['category'] = base64_encoding(knowledgerank_doc['category'])
                # knowledge_dict['title'] = base64_encoding(knowledgerank_doc['title'])
                # knowledge_dict['body'] = base64_encoding(knowledgerank_doc['body'])
                knowledge_dict['keyword_title'] = base64_encoding(knowledgerank_doc['keyword_title'])
                knowledge_dict['scope_list'] = knowledgerank_doc['scope_list']

                knowledge_lists = ['new1_id', 'new2_id', 'top1_id', 'top2_id', 'top3_id', 'top4_id', 'top5_id', 'ran1_id', 'ran2_id']
                for knowledge_object in knowledge_lists:
                        if knowledge_object in knowledgerank_doc :
                               knowledge_dict[knowledge_object] = str(knowledgerank_doc[knowledge_object])
                knowledge_list.append(knowledge_dict)


        # 동영상 구문 시작 
        #각 도큐먼트를 한개씩 조회
        for videorank_doc in db.videorank.find():
            flag = True;

            # 문진결과와 복수조건 비교
            for scope_value in videorank_doc['scope_list']:
                scope = convert_to_dict(scope_value)
                # print(scope)
                operator = str(scope['operator'])
                operand = scope['operand']
                sur_key = scope['sur_key']

                if sur_key in survey_data['survey_data'] :
                    sur_value = survey_data["survey_data"][sur_key]
                    # print("sur_value : " + str(sur_value))
                    # print("operand : " + str(operand))
                    # print("sur_key : " + str(sur_key))
                    #DB에 저장된 조건이 '=' 혹은 '==' 일 때
                    if eq(operator, '=') or eq(operator, '=='):
                        if not float(sur_value) == float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<'일 때
                    elif eq(operator, '<'):
                        if not float(sur_value) < float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>'일 때
                    elif eq(operator, '>'):
                        if not float(sur_value) > float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '<=' 혹은 '=<'일 때
                    elif eq(operator, '<=') or eq(operator, '=<'):
                        if not float(sur_value) <= float(operand):
                            flag = False;
                            break;
                    #DB에 저장된 조건이 '>=' 혹은 '=>'일 때
                    elif eq(operator, '>=') or eq(operator, '=>'):
                        if not float(sur_value) >= float(operand):
                            flag = False;
                            break;
                else : 
                    flag = False;

            #모든 복수조건을 만족하면 링크 정보를 dict형으로 video_list에 추가
            if flag:
                video_dict = {}
                video_dict['id'] = str(videorank_doc['_id'])
                # video_dict['category'] = base64_encoding(video_doc['category'])
                video_dict['keyword_title'] = base64_encoding(videorank_doc['keyword_title'])
                video_dict['category'] = base64_encoding(videorank_doc['category'])
                # video_dict['title'] = base64_encoding(videorank_doc['title'])
                # video_dict['body'] = base64_encoding(videorank_doc['body'])
                video_dict['scope_list'] = videorank_doc['scope_list']

                video_lists = ['new1_id', 'new2_id', 'top1_id', 'top2_id', 'top3_id', 'top4_id', 'top5_id', 'ran1_id', 'ran2_id']
                for video_object in video_lists:
                       if video_object in videorank_doc :
                              video_dict[video_object] = str(videorank_doc[video_object])


                video_list.append(video_dict)




        print(json.dumps({'code': 100, 'msg': 'True', 'result': link_list, 'result_knowledge': knowledge_list, 'result_video': video_list}, ensure_ascii=False))





        #return {'code' : 100, 'msg' : 'True', 'result': link_list}

    except Exception as e:
        print(e)
        print(json.dumps({'code': 1, 'msg': 'False'}, ensure_ascii=False))
        #return {'code': 1, 'msg': 'False'}


if __name__=='__main__':
    contents(sys.argv[1])

#테스트 직렬화데이터(중년 폐암) : 0000011960051217608840000100000000100000000000001000000000000000000
