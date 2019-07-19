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

    result[movieCd] = {
        '영화코드' : movieCd,
        '영화이름' : response['movieInfoResult']['movieInfo']['movieNm'],
        '영화이름(영문)' : response['movieInfoResult']['movieInfo']['movieNmEn'],
        '영화이름(원문)' :response['movieInfoResult']['movieInfo']['movieNmOg'] if response['movieInfoResult']['movieInfo']['movieNmOg'] else None,
        '관람등급' : response['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'] if response['movieInfoResult']['movieInfo']['audits'] else None ,
        '개봉연도' : response['movieInfoResult']['movieInfo']['openDt'],
        '상영시간' : response['movieInfoResult']['movieInfo']['showTm'],
        '장르' : response['movieInfoResult']['movieInfo']['genres'][0]['genreNm'] if response['movieInfoResult']['movieInfo']['genres'] else None,
        '감독' : response['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'] if response['movieInfoResult']['movieInfo']['directors'] else None
    }
# 적어봅시다.
with open('movie.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화이름', '영화이름(영문)', '영화이름(원문)','관람등급', '개봉연도', '상영시간', '장르', '감독']  
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result.values():
      csv_writer.writerow(item)

        
