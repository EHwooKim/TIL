import datetime
import requests
import csv
from decouple import config


result = {}
for i in range(49,-1,-1):
    targetDt = (str(datetime.date(2019, 7, 13) - datetime.timedelta(weeks=i))).replace('-', '')
    # targetDt = datetime.date(2019, 7, 13) - datetime.timedelta(weeks=i)
    # targetDt = targetDt.strftime('%Y%m%d')
    
    key = config('KEY')
    weekGb = '0'
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    response = requests.get(api_url).json()

    
    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
        
        result[movie.get('movieCd')] = {
                                        '영화코드': movie.get('movieCd'),
                                        '영화이름': movie.get('movieNm'),
                                        '누적관객수': movie.get('audiAcc')
                                        }


with open('boxoﬃce.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화이름', '누적관객수']  
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()  
    for item in result.values():
        csv_writer.writerow(item)

          