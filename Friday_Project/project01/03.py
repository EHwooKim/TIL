import requests
import csv
from decouple import config


result = {}
name_list=[]
with open('movie.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        name_list.append(line['감독'])

for name in name_list:
    key = config('KEY')
    peopleNm = name
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'
    response = requests.get(api_url).json()

    if name == None:
        continue
    result[name] = {
                    '영화인 코드': response['peopleListResult']['peopleList'][0]['peopleCd'] if response['peopleListResult']['peopleList'] else None,
                    '영화인명': response['peopleListResult']['peopleList'][0]['peopleNm'] if response['peopleListResult']['peopleList'] else None,
                    '분야': response['peopleListResult']['peopleList'][0]['repRoleNm'] if response['peopleListResult']['peopleList'] else None,
                    '필모리스트': response['peopleListResult']['peopleList'][0]['filmoNames'] if response['peopleListResult']['peopleList'] else None
                    }

    
with open('director.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화인 코드', '영화인명', '분야', '필모리스트']  
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result.values():
      csv_writer.writerow(item)

