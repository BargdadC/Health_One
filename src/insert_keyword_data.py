# 파일 : insert_keyword_data.py
# 용도 : 키워드셋을 한꺼번에 삽입합니다.

# -*- coding: utf8 -*-
import pymongo
from datetime import datetime

#커넥션 생성
connection = pymongo.MongoClient('localhost', 27017)
db = connection.Health_One

default_time = datetime.now()

def insert_keyword_data():

    db.keyword.insert_one(
    {
        u'category' : u'신체조건',
        u'scope_list' : ['con_bmi<18.5'],
        u'keyword_title' : u'저체중',
        u'keyword_list' : [u'저체중 위험', u'저체중 극복', u'저체중 식단'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'신체조건',
        u'scope_list' : ['con_bmi>23','con_bmi<=25'],
        u'keyword_title' : u'과체중',
        u'keyword_list' : [u'과체중 위험', u'과체중 극복', u'과체중 식단'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'신체조건',
        u'scope_list' : ['con_bmi>25'],
        u'keyword_title' : u'비만',
        u'keyword_list' : [u'비만 위험성', u'비만 극복', u'비만 식단'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_meal<=1'],
        u'keyword_title' : u'소식',
        u'keyword_list' : [u'하루 한끼 이하', u'불규칙적 식사의', u'불규칙적 식사에'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_meal==4'],
        u'keyword_title' : u'과식',
        u'keyword_list' : [u'과식의 원인', u'과식의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_nightmeal>=5'],
        u'keyword_title' : u'야식',
        u'keyword_list' : [u'야식의 위험', u'야식 증후군'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_cataract==TRUE'],
        u'keyword_title' : u'눈(백내장)',
        u'keyword_list' : [u'백내장의 원인', u'백내장 극복', u'백내장의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_glaucoma==TRUE'],
        u'keyword_title' : u'눈(녹내장)',
        u'keyword_list' : [u'녹내장의 원인', u'녹내장 극복', u'녹내장의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_dry==TRUE'],
        u'keyword_title' : u'눈(안구건조증)',
        u'keyword_list' : [u'안구건조증의 원인', u'안구건조증 극복', u'안구건조증의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_presbyopia==TRUE'],
        u'keyword_title' : u'눈(노안)',
        u'keyword_list' : [u'노안의 극복', u'노안의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_myopia==TRUE'],
        u'keyword_title' : u'눈(근시)',
        u'keyword_list' : [u'근시의 원인', u'근시의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_hperopia==TRUE'],
        u'keyword_title' : u'눈(원시)',
        u'keyword_list' : [u'원시의 원인'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_astigmatism==TRUE'],
        u'keyword_title' : u'눈(난시)',
        u'keyword_list' : [u'난시의 원인', u'난시 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_strabismus==TRUE'],
        u'keyword_title' : u'눈(사시)',
        u'keyword_list' : [u'눈 사시 위험', u'눈 사시 교정'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['ear_tinnitus==TRUE'],
        u'keyword_title' : u'귀(이명)',
        u'keyword_list' : [u'이명의 원인', u'이명 극복', u'이명의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['ear_tympanitis==TRUE'],
        u'keyword_title' : u'귀(중이염)',
        u'keyword_list' : [u'중이염의 원인', u'중이염 극복', u'중이염의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['ear_impairment==TRUE'],
        u'keyword_title' : u'귀(난청)',
        u'keyword_list' : [u'난청의 원인', u'난청 극복', u'난청의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_obstructive==TRUE'],
        u'keyword_title' : u'호흡기(만성폐쇄성질환)',
        u'keyword_list' : [u'만성폐쇄성질환 극복', u'만성폐쇄성질환의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_tuberculosis==TRUE'],
        u'keyword_title' : u'호흡기(폐결핵)',
        u'keyword_list' : [u'폐결핵 치료', u'폐결핵의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_cough==TRUE'],
        u'keyword_title' : u'호흡기(만성기침)',
        u'keyword_list' : [u'만성기침의 원인', u'만성기침 극복', u'만성기침의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_asthma==TRUE'],
        u'keyword_title' : u'호흡기(천식)',
        u'keyword_list' : [u'천식의 원인', u'천식 극복', u'천식의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_pneumonia==TRUE'],
        u'keyword_title' : u'호흡기(폐렴)',
        u'keyword_list' : [u'폐렴의 원인', u'폐렴 극복', u'폐렴의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['r_rhinitis==TRUE'],
        u'keyword_title' : u'호흡기(비염)',
        u'keyword_list' : [u'비염의 원인', u'비염 극복', u'비염의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_allergy==TRUE'],
        u'keyword_title' : u'피부(알레르기)',
        u'keyword_list' : [u'피부 알레르기의 원인', u'피부 알레르기 극복', u'피부 알레르기의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_alopecia==TRUE'],
        u'keyword_title' : u'피부(탈모)',
        u'keyword_list' : [u'탈모의 원인', u'탈모 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_cancer==TRUE'],
        u'keyword_title' : u'피부(피부암)',
        u'keyword_list' : [u'피부암의 원인', u'피부암 극복', u'피부암의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_acne==TRUE'],
        u'keyword_title' : u'피부(여드름)',
        u'keyword_list' : [u'여드름의 원인', u'여드름 극복', u'여드름의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_atopic==TRUE'],
        u'keyword_title' : u'피부(아토피)',
        u'keyword_list' : [u'아토피의 원인', u'아토피 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_vitiligo==TRUE'],
        u'keyword_title' : u'피부(백반증)',
        u'keyword_list' : [u'백반증의 원인', u'백반증 극복', u'백반증의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_psoriasis==TRUE'],
        u'keyword_title' : u'피부(건선)',
        u'keyword_list' : [u'건선의 원인', u'건선 극복', u'건선의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['ger_hypertension==TRUE'],
        u'keyword_title' : u'성인병(고혈압)',
        u'keyword_list' : [u'고혈압의 원인', u'고혈압 극복', u'고혈압의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['ger_diabets==TRUE'],
        u'keyword_title' : u'성인병(당뇨병)',
        u'keyword_list' : [u'당뇨병의 원인', u'당뇨병 극복', u'당뇨병의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_liver==TRUE'],
        u'keyword_title' : u'암(간암)',
        u'keyword_list' : [u'간암의 원인', u'간암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_stomach==TRUE'],
        u'keyword_title' : u'암(위암)',
        u'keyword_list' : [u'위암의 원인', u'위암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_lung==TRUE'],
        u'keyword_title' : u'암(폐암)',
        u'keyword_list' : [u'폐암의 원인', u'폐암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_thyroidGland==TRUE'],
        u'keyword_title' : u'암(갑상선암)',
        u'keyword_list' : [u'갑상선암의 원인', u'갑상선암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_breast==TRUE'],
        u'keyword_title' : u'암(유방암)',
        u'keyword_list' : [u'유방암의 원인', u'유방암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_other==TRUE'],
        u'keyword_title' : u'암(기타)',
        u'keyword_list' : [u'암의 원인', u'암 극복'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['fam_stroke==TRUE'],
        u'keyword_title' : u'가족력(뇌졸증/중풍)',
        u'keyword_list' : [u'뇌졸증 가족력', u'증풍 가족력'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['fam_myocardialInfarction==TRUE'],
        u'keyword_title' : u'가족력(심근경색/협심증)',
        u'keyword_list' : [u'심근경색 가족력', u'협심증 가족력'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['fam_hypertension==TRUE'],
        u'keyword_title' : u'가족력(고혈압)',
        u'keyword_list' : [u'고혈압 가족력'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['fam_diabetes==TRUE'],
        u'keyword_title' : u'가족력(당뇨병)',
        u'keyword_list' : [u'당뇨병 가족력'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['fam_cancer==TRUE'],
        u'keyword_title' : u'가족력(암)',
        u'keyword_list' : [u'암 가족력'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_drink_time>=5'],
        u'keyword_title' : u'잦은 음주',
        u'keyword_list' : [u'잦은 음주 극복', u'잦은 음주의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_drink_intake>=4'],
        u'keyword_title' : u'과음',
        u'keyword_list' : [u'과음 극복', u'과음의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_smoke==3'],
        u'keyword_title' : u'흡연',
        u'keyword_list' : [u'흡연 극복', u'흡연의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_exercise<=2'],
        u'keyword_title' : u'운동부족',
        u'keyword_list' : [u'운동부족 극복', u'운동부족의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['h_exercise>=6'],
        u'keyword_title' : u'운동과다',
        u'keyword_list' : [u'운동과다의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['con_bmi>=25', 'h_menu==4'],
        u'keyword_title' : u'비만 과식',
        u'keyword_list' : [u'살찐 사람 과식'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['con_bmi>=25', 'h_nightmeal>=6'],
        u'keyword_title' : u'비만 야식',
        u'keyword_list' : [u'비만인 야식의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['con_bmi>=25', 'h_smoke==3'],
        u'keyword_title' : u'비만 흡연',
        u'keyword_list' : [u'비만 흡연자 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['con_bmi>=25', 'h_drink_time>=5'],
        u'keyword_title' : u'비만 잦은음주',
        u'keyword_list' : [u'살찐 사람 음주의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['con_bmi>=25', 'h_exercise<=1'],
        u'keyword_title' : u'비만 운동부족',
        u'keyword_list' : [u'비만인 운동', u'비만인 운동의 위험'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['can_liver==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'간암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['can_stomach==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'위암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'생활습관',
        u'scope_list' : ['can_lung==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'폐암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_thyroidGland==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'갑상선암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_breast==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'유방암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_other==TRUE', 'h_drink_intake==4'],
        u'keyword_title' : u'기타암 음주',
        u'keyword_list' : [u'암 환자 음주', u'암 환자 과음'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_liver==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'간암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_stomach==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'위암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_lung==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'폐암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_thyroidGland==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'갑상선암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_breast==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'유방암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_other==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'기타암 흡연',
        u'keyword_list' : [u'암 환자 흡연'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_liver==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'간암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_stomach==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'위암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_lung==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'폐암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_thyroidGland==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'갑상선암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_breast==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'유방암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['can_other==TRUE', 'h_exercise<=1'],
        u'keyword_title' : u'기타암 운동부족',
        u'keyword_list' : [u'암 환자 운동', u'암 환자 운동부족'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_atopic==TRUE', 'h_drink_time>=5'],
        u'keyword_title' : u'아토피 과음',
        u'keyword_list' : [u'아토피 음주'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['eye_dry==TRUE', 'h_smoke==3'],
        u'keyword_title' : u'안구건조증 흡연',
        u'keyword_list' : [u'흡연자 안구건조'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['skin_acne==TRUE', 'h_nightmeal>=6'],
        u'keyword_title' : u'여드름 야식',
        u'keyword_list' : [u'여드름 야식'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['con_gender==1', 'con_age>=50', 'h_smoke==3'],
        u'keyword_title' : u'남성 50세이하 흡연',
        u'keyword_list' : [u'흡연 정자', u'흡연 발기부전'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['con_gender==2', 'con_age>=50', 'h_smoke==3'],
        u'keyword_title' : u'여성 50세이하 흡연',
        u'keyword_list' : [u'여성 흡연 난임', u'흡연 조기 폐경'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['con_gender==1', 'con_age>=50', 'h_drink_time>=5'],
        u'keyword_title' : u'남성 50세이하 음주',
        u'keyword_list' : [u'음주 정자', u'음주 발기부전'],
        u'last_update' : default_time
    })

    db.keyword.insert_one(
    {
        u'category' : u'질병',
        u'scope_list' : ['con_gender==2', 'con_age>=50', 'h_drink_time>=5'],
        u'keyword_title' : u'여성 50세이하 음주',
        u'keyword_list' : [u'여성 음주 난임', u'음주 조기 폐경'],
        u'last_update' : default_time
    })
    

insert_keyword_data()
