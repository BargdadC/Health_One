# -*- coding: utf8 -*-
import sys
import base64
import json
import requests
import urllib.request
from bs4 import BeautifulSoup
from pyowm import OWM

def get_weather(lat, lon):
	try:
		# owm api - 날씨
		# id : afewgm20@gmail.com
		# pw : afewgm.20
		# key : a5486ad8df5934ae8df439dae0f2bb9e
		owm_api_key = 'a5486ad8df5934ae8df439dae0f2bb9e'
		owm = OWM(owm_api_key)
		obs = owm.weather_at_coords(float(lat), float(lon))
		w = obs.get_weather()

		temperature = round(w.get_temperature(unit='celsius')['temp'])
		'''
		print(w.get_temperature(unit='celsius')['temp'])
		print(w.get_temperature(unit='celsius')['temp_max'])
		print(w.get_temperature(unit='celsius')['temp_min'])
		'''	
		status = w.get_status()
		#status = w.get_detailed_status()
		status_icon = w.get_weather_icon_name() + '.png'



		# airvisual api - 미세먼지
		# id : afewgm20@gmail.com
		# pw : afewgm.20
		# key : xusP8FYT37dwaAcox
		try:
			airvisual_api_key = "xusP8FYT37dwaAcox"
			url = ("http://api.airvisual.com/v2/nearest_city?lat=" + str(lat) + "&lon=" + str(lon) + "&rad=500&key=" + airvisual_api_key)
			html = urllib.request.urlopen(url)
			soup = BeautifulSoup(html,"lxml")
			p_tag = soup.find('p')
			airvisual_results = json.loads(p_tag.text)

			find_dust = airvisual_results['data']['current']['pollution']['aqius']

		except:
			find_dust = 0



		'''
		# google api - 주소 변환
		try:
			url = ("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=" + str(lat) + "," + str(lon))
			html = urllib.request.urlopen(url)
			soup = BeautifulSoup(html,"lxml")
			p_tag = soup.find('p')
			google_results = json.loads(p_tag.text)
		
			address = google_results['results'][0]['formatted_address']

		except:
			address = "구글맵...유료 전환"
		'''



		# kakao api - 주소 변환
		# id : 01022490633
		# pw : 
		# key : 4e31224870867934fc18a033e6475053
		try:
			kakao_api_key = '4e31224870867934fc18a033e6475053'
			url="https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=" + str(lon) + "&y=" + str(lat)
			headers = {'Authorization': 'KakaoAK ' + kakao_api_key, 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
			r = requests.get(url,headers=headers)
			r.get_method = lambda:"GET"
			response_body = r.json

			content_bytes = r.content
			content_encoded = base64.b64encode(content_bytes)
			content_decoded = str(base64.b64decode(content_encoded), encoding='utf-8')
			content_dic = json.loads(content_decoded)

			r.close

			address = content_dic['documents'][1]['address_name']

		except:
			address = "충청북도 충주시 건국대학교 글로컬캠퍼스"



		'''
		# naver api - 상태 변환
		# naver id : kimjg0616
		# naver pw : 
		# key id : W7VcmzK7THMgnOBJD_P6
		# key secret : ELtRu0W0BY
		client id = "W7VcmzK7THMgnOBJD_P6"
		client secret = "ELtRu0W0BY"
		encText = urllib.parse.quote(w.get_status())
		data = "source=en&target=ko&text=" + encText
		url = "https://openapi.naver.com/v1/papago/n2mt"
		request = urllib.request.Request(url)
		request.add_header("X-Naver-Client-Id",client_id)
		request.add_header("X-Naver-Client-Secret",client_secret)
		response = urllib.request.urlopen(request, data=data.encode("utf-8"))
		rescode = response.getcode()
		response_body = response.read()
		naver_results = json.loads(response_body.decode('utf-8'))

		status = naver_results['message']['result']['translatedText']
		'''


		
		# 상태 변환, 날씨 이미지 url : http://openweathermap.org/img/w/$weather_img
		if status == 'Clear':
			status_ko = '맑음'
		elif status == 'Rain':
			status_ko = '비'
		elif status == 'Clouds':
			status_ko = '구름'
		elif status == 'Haze':
			status_ko = '안개(연무)'
		elif status == 'Mist':
			status_ko = '안개(박무)'
		elif status == 'Fog':
			status_ko = '짙은 안개'
		elif status == 'Snow':
			status_ko = '눈'
		elif status == 'Sand':
			status_ko = '황사'
		elif status == 'Dust':
			status_ko = '먼지'
		elif status == 'Thunderstorm':
			status_ko = '뇌우'
		elif status == 'Smoke':
			status_ko = '연기'
		elif status == 'Drizzel':
			status_ko = '이슬비'

		# 미세먼지 수치에 따른 상태 변환
		if(find_dust <= 50):
			find_dust_status = "좋음"
		elif(find_dust <= 100):
			find_dust_status = "보통"
		else:
			find_dust_status = "나쁨"


		'''
		# 웹에서 한글을 받을 때 오류 발생 -> 값에 한글이 들어가는 주소, 날씨(상태), 기온, 미세먼지 상태 변수 base64로 인코딩
		address_bytes = address.encode()
		address_base64 = base64.b64encode(address_bytes)
		address_en = str(address_base64)[2:-1]

		status_bytes = status_ko.encode()
		status_base64 = base64.b64encode(status_bytes)
		status_en = str(status_base64)[2:-1]

		find_dust_status_bytes = find_dust_status.encode()
		find_dust_status_base64 = base64.b64encode(find_dust_status_bytes)
		find_dust_status_en = str(find_dust_status_base64)[2:-1]
		'''
		dic_en = {'address':address, 'status_ko':status_ko, 'find_dust_status':find_dust_status}
		for v in dic_en:
			dic_en[v] = dic_en[v].encode()
			dic_en[v] = base64.b64encode(dic_en[v])
			dic_en[v] = str(dic_en[v])
		
		print(json.dumps({'code' : 100, 'msg' : "True", 'lat' : lat, 'lon' : lon, 'address_en' : dic_en['address'][2:-1], 'status' : status, 'status_en' : dic_en['status_ko'][2:-1], 'weather_img' : "http://openweathermap.org/img/w/" + status_icon, 'temperature' : temperature, 'find_dust' : find_dust, 'find_dust_status_en' : dic_en['find_dust_status'][2:-1]},ensure_ascii=False))
		
	except:
		#print(json.dumps({'code' : 1, 'msg' : "False", 'lat' : lat, 'lon' : lon}, ensure_ascii=False))
		get_weather(sys.argv[1] ,sys.argv[2])


if __name__=='__main__':
	try:
		if sys.argv[3] != "":
			print(json.dumps({'code' : 2, 'msg' : "False"},ensure_ascii=False))

	except:
		try:
			get_weather(sys.argv[1] ,sys.argv[2])
		
		except:
			print(json.dumps({'code' : 2, 'msg' : "False"},ensure_ascii=False))
			