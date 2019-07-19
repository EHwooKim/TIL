# 파이썬을 활용한 데이터 수집 I 

##  영화진흥위원회 API를 활용한 영화 정보 수집

* [영화진흥위원회 오픈 API](http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)
* URL에서  `.xml` , `.json` 확인하기.

### 00. csv 파일 읽고 쓰기

* `csv(comma separated value)` : 쉼표를 기준으로 항목을 구분하여 저장한 데이터 

* 쓰기

  ```python
  import csv
  
  with open('boxoﬃce.csv','w',encoding='utf-8') as f:
      fieldnames = ['영화코드', '영화이름', '누적관객수']  
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()  
      for item in result.values():
          csv_writer.writerow(item)	
  ```

* 읽기

  ```python
  import csv
  
  with open('boxoﬃce.csv', 'r', encoding='utf-8') as f:
      csv_reader = csv.DictReader(f)
      for line in csv_reader:
          code_list.append(line['영화코드'])
  ```

  >`DictWritet`,  `DictReader`을 활용하면 cvs 파일을 딕셔너리로 활용이 가능해서 편하다.
  >
  > 쓸 때는 정해진 key에 맞는 value이 들어가고
  >
  > 읽을 때도 key로 원하는 value를 가져올 수 있다.

  * 나는 처음에 code_list.append(line[7])과 같은 방법으로 값을 가져와서 잘못가져오기도 했었다.

### 01. 주간 박스오피스

* API

  ```python
  import requests
  
  key = config('KEY')
  weekGb = '0'   # default - '1' : 주말 (금~일) 
  api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'
  response = requests.get(api_url).json()
  ```

* 키값은 `환경변수`로 처리하기.

     ```python
     #.env 파일
     KEY='__Key__'
     
     # key를 사용하는 파일
     from decouple import config
     key = config('KEY')
     ```

* 날짜 계산

  ```python
  import datetime
  
  for i in range(49,-1,-1):
      # 방법1
      targetDt = (str(datetime.date(2019, 7, 13) - datetime.timedelta(weeks=i))).replace('-', '')
      # 방법2.
      targetDt = datetime.date(2019, 7, 13) - datetime.timedelta(weeks=i)
      targetDt = targetDt.strftime('%Y%m%d')
  ```
  
  * `datetime` 
  
    * `datetime.date`와 `datetime.timedelta`를 이용하여 날짜 계산,
  
      반환값이 `2019-07-13`과 같은 형태라`str `, `replace`를 이용하여`20190713`형태로 바꿔줬다.
  
    * 방법2
  

### 02. 영화 상세정보

* API

  ```python
  import requests
  
  key = config('KEY')
  movieCd = code
  api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
  response = requests.get(api_url).json()
  ```

* `list index out of range` 오류

  ```python
  movie_info = response['movieInfoResult']['movieInfo']
  result[movieCd] = {
  	'영화코드' : movieCd,
  		...
      '관람등급' : movie_info['audits'][0]['watchGradeNm'] if movie_info['audits'] else None 
  }
  ```

  * 리스트 `movie_info['audits'] ` 가 비어있을 때도 있어서 `list index out of range` 오류가 발생

    `조건 표현식`으로 예외처리

    

### 03. 영화인 정보

* API

  ```python
  import requests
  
  key = config('KEY')
  peopleNm = name
  api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'
  response = requests.get(api_url).json()
  ```


