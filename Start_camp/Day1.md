# Startcamp Day1

## Python 기초 문법

//"#한개, #두개로 제목설정"

1. 저장

   ``` Python
   # ```Python치면 이런 코드 블록 생성
   
   # 저장은 =을 통해서 한다. 
   dust = 64 #숫자(integer)
   name = '홍길동' #문자열(string)
   is_summer = True #참/거짓, Boolean(True/False)
   ```

   ```Python
   # 리스트 활용법
   my_list = [1,2,3,'정지수','염겨례']
   print(my_list[0]) # => 1
   # 딕셔너리 활용법
   my_dictionary = {'정지수':'남자'.'염겨례':'남자'}
   print(my_dictionary['정지수']) # => '남자'
   ```

   

2. 조건

   ```Python
   if dust > 150:
       print('매우나쁨')
   elif dust > 80:
       print('나쁨')
   else:
       print('보통')
   ```

   

3. 반복

   ```Python
   lunch_box = ['짬뽕',  '돈까스', '김치볶음밥']
   # 정해진 리스트 반복
   for menu in lunch_box:
       print(menu)
       # menu = lunch_box[0], ... , menu = lunch_box[2]
       
   # n번 반복
   for i in range(5):
       print('hello!!')
       
       	
   ```

4. 내장함수

   > 내장함수는 별도로 import 구문이 필요하다  
   >
   > (">하면 이렇게 앞쪽에 막대바, Ctrl + / 누르면 타이핑  한 것 그대로 보여줌") 

   ```Python
   print('hi')
   print(max([2, 4, 1])) #=> 4
   print(min([1, 2, 5])) #=> 1
   print(abs(-5)) #=> 5
   print(len([1, 2, 3])) #=> 3
   ```

5. 외장함수

   > 외장함수는 반드시  import가 필요하다.
   >
   > 다만, 파이썬을 설치하면 그냥 불러서 쓸 수 있다.

   ```Python
   import random
   numbers = range(1,46)
   lotto = random.sample(numbers,6) # 한개 선택시 random.choice
   print(sorted(lotto)) # sorted : 정렬
   ```

6. 패키지

   > 패키지는 반드시 설치를 필요로 한다.

   `pip install 패키지명` 으로 설치를 한다.  // " `한개로묶으면 이렇게 포인트"

   ```bash
   $ pip install requests  # 앞에 $표시 있는 것은 git bash 입력하는 명령어를 의미
   requests.get(url) # 와 같이 사용을 한다.
   ```



## 파이썬을 통한 크롤링

1. 필수 설치 패키지

   * requests : 파이썬으로 요청을 보내주는 패키지 // *하고 띄어쓰면 다음과 같은 순서없는 목록

   * bs4 : 문자열을 html 등으로 구조화(파싱)를 해주는 패키지

     ```bash
     $ pip install requests
     $ pip install bs4
     ```

2. 네이버에서 코스피지수 가져오기

   ```Python
   # 0. 활용할 패키지를 불러온다.
   import requests
   from bs4 import BeautifulSoup  # 이런 모양의 변수명을 Camel case
   # 1. url을 설정한다.
   url = 'https://finance.naver.com/sise'
   # 2. 요청을 보내고, 그 결과의 내용을(text) response에 저장한다.
   response = requests.get(url).text
   # 3. html 문서로 변환한다.
   soup = BeautifulSoup(response, 'html.parser')
   # 4. 원하는 값을 선택자(selector)를 활용해서 가져온다.
   kospi = soup.select_one('#KOSPI_now').text # 이런 모양의 변수명을 Snake case
   print(kospi)
   ```

   