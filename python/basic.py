import requests



key = '9c9222c3292d5e4039f7e78c54fe4100'
targetDt = '20190713'  #yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'

print(api_url)
response = requests.get(api_url).json()
print(response)

