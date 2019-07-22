import csv
import requests
from decouple import config



result ={}
code_list = []

with open('boxoﬃce.csv', 'r', encoding='utf-8') as f:
    # 어찌어찌 영화 코드를 뽑아서
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        code_list.append(line['영화코드'])
# 코드먼저 뽑아서 리스트에 담아놓고 boxoffice 파일은 닫아버려

for code in code_list:
    key = config('KEY')
    movieCd = code
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'

    response = requests.get(api_url).json()
    movoe_info = response['movieInfoResult']['movieInfo']
    result[movieCd] = {
        '영화코드' : movieCd,
        '영화이름' : movoe_info['movieNm'],
        '영화이름(영문)' : movoe_info['movieNmEn'],
        '영화이름(원문)' :movoe_info['movieNmOg'] if movoe_info['movieNmOg'] else None,
        '관람등급' : movoe_info['audits'][0]['watchGradeNm'] if movoe_info['audits'] else None ,
        '개봉연도' : movoe_info['openDt'],
        '상영시간' : movoe_info['showTm'],
        '장르' : movoe_info['genres'][0]['genreNm'] if movoe_info['genres'] else None,
        '감독' : movoe_info['directors'][0]['peopleNm'] if movoe_info['directors'] else None
    }
# 적어봅시다.
with open('movie.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화이름', '영화이름(영문)', '영화이름(원문)','관람등급', '개봉연도', '상영시간', '장르', '감독']  
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result.values():
      csv_writer.writerow(item)

        
