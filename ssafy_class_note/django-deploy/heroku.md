* 헤로쿠에 우리 환경을 알려주기 위한 설정!

  * `runtime.txt` 생성
    * python-3.7.1
  * `Procfile` 생성
    * web: gunicorn lastProject.wsgi --log-file -  (띄어쓰기 주의!!)

  ```bash
  $ pip install gunicorn
  $ pip install django-heroku
  $ pip freeze > requirements.txt
  ```

  ```bash
  $ heroku 
  ```

  * 검색해봐서
  * 뭔가 없다 그러면 heroku cli 설치

  ```bash
  $ heroku login
  ```

  * production.py 에

    ```python
    import django_heroku
    django_heroku.settings(locals())
    ```

    추가

  ```bash
  heroku create __원하는 url 이름__
  ```

  ```bash
  $ git push heroku master
  ```

  >  ! [remote rejected] master -> master (pre-receive hook declined)
  > error: failed to push some refs to 'https://git.heroku.com/woobum.git'	

  오류 나면

  heroku.com 가서 settings 에서  vari 어쩌구에서 SECRET_KEY에 .env에 썼던거 쓰기

  ```bash
  heroku run python manage.py migrate
  ```

  * static을 쓰는데 이미지 로딩이 느리다면 
    * web image optimize
    * git 



* database 오류
* static 오류

* local은 컴퓨터꺼지면 서버 꺼지는데 demon..실시간으로 계속 돌아야 실사용가능한데 gunicorn으로 그걸 한다. (헤로쿠에서는 proc 파일 만든거)



## Vue 배포

* Vue는 https://app.netlify.com/start에서 new site from git 에서 원하는 vue선택하면된다.

* public 폴더안에 _redirects 파일(확장자없는) 만들어서 

  ```
  /* /index.html 200
  ```

* 마지막 buil d command에

  ```
  npm run build
  ```

  publih directory

  ```
  dist
  ```

  리액트에서 개츠비(?) 불러오고 할 때도 쓰인다.



