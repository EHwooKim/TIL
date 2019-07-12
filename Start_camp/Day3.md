# Day3

## HTML/CSS

### HTML

`HTML` 은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <title>Document</title>
   </head>
   <body>
       <h1>안녕?</h1>
   </body>
   </html>
   ```

   * `<head> </head>` 는 문서의 정보를 담고 있다.
   * `<body> </body>` 는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와 `닫는태그` 로 구성된다.

      ```html
      <h1>제목</h1>
      ```

   2. `닫는태그` 가 없는 경우도 있다.(self-closing tag)

      ```html
      <img src="__"/>
      ```

3. 태그의 구성

   ```html
   <img src="__" width="300" height="300".>
   <a href="http://google.com" class="blue">구글</a>
   ```

   * 태그별로 공통적으로 가질 수 있는 속성 : `id`, `class` , `style`
   * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     * img -`src`,`width`,`height`
     * a - `href`

### CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```css
     p {
         color: red;
     }
     ```

     

   * class 선택자

     ```css
     .blue {
         color: blue;
     }
     ```

     

   * id 선택자

     ```css
     #pink {
         color: pink;
     }
     ```

   선택자 우선순위는 id선택자 > class선택자 > 태그선택자 순으로 적용된다.



## Flask

`Flask`는 파이썬 기반의 micro framework이다.

### 기본 활용법



1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ = '__main__':
       app.run(debug=True)
   ```

3. 서버실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run` 명령어는 `app.py` 파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   * 마지막 두 줄을 작성해놓았따면, 아래와 같이 실행도 가능하다.

   ```bash
   $ python app.py
   ```


### Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?'
```

### Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_templates
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML`파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야 한다.

```python
return render_template('hi.html',name=name)
```

그리고 출력을 위해서`{{}}` 사용한다.

```jinja2
<h1>{{name}}안녕?</h1>
```

### Flask Template Engine - jinja2

Flask는 기본적으로 Template를 만들 때 `jinja2` 언어를 사용한다. 기본 문법은 다음과 같다.

1. 값 출력

   ```jinja2
   <h1> {{ name }}, 안녕? </h1
   ```

2. 조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요.</h1>
   {% else %}
   	<h1>학생들 ㅎㅇ</h1>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list %}
   	<li>{{ menu }}</li>
   {% endfor %}
   ```


### Form date

HTML에서 사용자로 부터 정보를 받기 위해서는 `form`태그를 활용한다.

#### form 태그 기본 구조

```html
<!-- templates/ping.html -->
<form action = '/pong'>
    <input type='text' name='say'>
    <input type='radio', name='gender', value='M'>남자
    <input type='submit' value='전송'>
</form>
```

* form 태그는 `action`속성으로 해당 폼이 전송될 url을 지정해야 한다.

* form 태그 내에는 `input` 태그들을 정의하여, 사용자에게 받을 정보를(설문지를만든다)

  만들어놓는다.

* `input` 태그에는 어떤 종류의 입력을 받을지(`type`)와 어떤 변수에 담아서 보낼지(`name`)정의한다.

### Flask에서 사용자로부터 정보 받기

1. 사용자가 입력할 수 있는 `form` 보내주기

   ```python
   # app.py
   @app.route('/ping')
   def ping():
       return render_template('ping.html')
   ```

   ```html
   <!-- templates/ping.html -->
   <form action = '/pong'>
       <input type='text' name='say'>
       <input type='submit' value='전송'>
   </form>
   ```

2. 정보 받아서 활용하기

   ```python
   # app.py
   from flask import Flask, render_template, request
   
   # ...
   
   @app.route('/pong')
   def pong():
       text = reqeust.args.get('say')
       return render_template('pong.html', say=say)
   ```

   ```html
   <!-- templates/pong.html -->
   <h1>{{ say }}!!!!</h1>
   ```

   * `request.args`는 일종의 `dictionary`이고, `key` : input에 정의한 name이고 사용자가 입력한 값은 `value` 이다.