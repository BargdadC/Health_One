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

#직렬화데이터에서 문진결과 값 반환
def extract_value(sur_str, sur_idx):
    value = 0

    #생년월일 8자리 int로 변환
    if sur_idx == 6:
        for i in range(0, 8):
            value *= 10
            value += int(sur_str[sur_idx+i])
    #키 3자리 int로 변환
    if sur_idx == 14:
        for i in range(0, 3):
            value *= 10
            value += int(sur_str[sur_idx+i])
    #몸무게 3자리 int로 변환
    if sur_idx == 17:
        for i in range(0, 3):
            value *= 10
            value += int(sur_str[sur_idx+i])
    #음주량 5자리 int로 변환
    if sur_idx == 60:
        for i in range(0, 5):
            value *= 10
            value += int(sur_str[sur_idx+i])
    #그 외의 경우
    if value == 0:
        value = int(sur_str[sur_idx])

    return value

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
    return {'sur_idx':scope[:oprt_start], 'operator':scope[oprt_start:oprt_end], 'operand':scope[oprt_end:]}

#pagerank 컬렉션을 순회하며 복수조건에 맞는 링크들의 정보를 추출
def contents(sur_str):
    link_list = [] #return될 링크들의 정보를 저장할 리스트

    try:
        #각 도큐먼트를 한개씩 조회
        for pagerank_doc in db.pagerank.find():
            flag = True;

            #문진결과와 복수조건 비교
            for scope_value in pagerank_doc['scope_list']:
                scope = convert_to_dict(scope_value)
                operator = scope['operator']
                operand = int(scope['operand'])
                sur_idx = int(scope['sur_idx'])
                sur_value = extract_value(sur_str, sur_idx)

                #DB에 저장된 조건이 '=' 혹은 '==' 일 때
                if eq(operator, '=') or eq(operator, '=='):
                    if not sur_value == operand:
                        flag = False;
                        break;
                #DB에 저장된 조건이 '<'일 때
                elif eq(operator, '<'):
                    if not sur_value < operand:
                        flag = False;
                        break;
                #DB에 저장된 조건이 '>'일 때
                elif eq(operator, '>'):
                    if not sur_value > operand:
                        flag = False;
                        break;
                #DB에 저장된 조건이 '<=' 혹은 '=<'일 때
                elif eq(operator, '<=') or eq(operator, '=<'):
                    if not sur_value <= operand:
                        flag = False;
                        break;
                #DB에 저장된 조건이 '>=' 혹은 '=>'일 때
                elif eq(operator, '>=') or eq(operator, '=>'):
                    if not sur_value >= operand:
                        flag = False;
                        break;

            #모든 복수조건을 만족하면 링크 정보를 dict형으로 link_list에 추가
            if flag:
                link_dict = {}
                link_dict['id'] = str(pagerank_doc['_id'])
                link_dict['category'] = base64_encoding(pagerank_doc['category'])
                link_dict['keyword_title'] = base64_encoding(pagerank_doc['keyword_title'])
                link_dict['scope_list'] = pagerank_doc['scope_list']
                link_dict['new1_id'] = str(pagerank_doc['new1_id'])
                link_dict['new2_id'] = str(pagerank_doc['new2_id'])
                link_dict['top1_id'] = str(pagerank_doc['top1_id'])
                link_dict['top2_id'] = str(pagerank_doc['top2_id'])
                link_dict['top3_id'] = str(pagerank_doc['top3_id'])
                link_dict['top4_id'] = str(pagerank_doc['top4_id'])
                link_dict['top5_id'] = str(pagerank_doc['top5_id'])
                link_dict['ran1_id'] = str(pagerank_doc['ran1_id'])
                link_dict['ran2_id'] = str(pagerank_doc['ran2_id'])
                link_list.append(link_dict)

        print(json.dumps({'code': 100, 'msg': 'True', 'result': link_list}, ensure_ascii=False))
        #return {'code' : 100, 'msg' : 'True', 'result': link_list}

    except Exception as e:
        print(e)
        print(json.dumps({'code': 1, 'msg': 'False'}, ensure_ascii=False))
        #return {'code': 1, 'msg': 'False'}


if __name__=='__main__':
    contents(sys.argv[1])

#테스트 직렬화데이터(중년 폐암) : 0000011960051217608840000100000000100000000000001000000000000000000
