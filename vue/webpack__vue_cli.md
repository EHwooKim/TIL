JS는 모듈의 개념이 없다. (태생이 브라우저 조작 언어였기 때문에)

script 주소를 이용해 load 하는 형태로 다양한 것들을 썼는데 node 이후로 모듈 개념으로 나온 것이 `webpack`



* Js를 윈도우 환경에서 쓰기 위해 설치한게 node



* `webpack`

노드기반의 라이버리를 활용하기 위해서

pip 같은 패키지 매니저인 npm을 설정해줘야한다

`npm init` -> `엔터엔터엔터엔터엔터엔터엔터엔터엔터 ` 하면 JSON 파일이 하나 생길거다

그 JSON 파일이 requirements 파일같이 버전관리 해주는 그거 



npm install vue

npm istall webpack webpack-cli -D (-D는 개발자버전)



`webpack.config.js` 파일 생성

 

기본적으로 해당 폴더(?)에 설치되고글로벌로 설치하려면 추가 명령어가 필요

* npm

  ```bash
  $ npm init
  ```

  * 비어있는 `package.json` 생성

* vue, webpack 설치

  ```bash
  $ npm install vue
  ```

  ```bash
  $ npm install webpack webpack-cli -D
  ```

  * webpack은 개발환경에서 `모듈 번들러`로써 활용하기 위한 것으로 `-D`옵션을 통해 `package.json`에서  `DevDependencies`에 추가

## Vue 개발환경

### 1. Vue 파일

> vue 파일들을 번역, 불러오기 위한 작업들

* vue 파일들을 번역, 불러오기 위한 작업들

```bash
npm install vue-loader vue-template-compiler -D
```

* vue-loader : vue 파일을 불러오는 역할
* vue-template-compiler : 해석하는 역할



* 꼬부랑 어쩌구 써있는 app.js를 만들었고 그걸 우리는

  ```html
    <script src="../dist/app.js"></script>
  ```

  이렇게 가져다 쓸 수 있다.



* 뭔가 변경되면 `npm run build`로 변경사항 적용





### 2. Style

> css 불러오기

```bash
$ npm install vue-style-loader css-loader -D
```

* vue-style-loader: vue의 style
* css-loader: webpack css 불러오는 로더

```js
// webpack.config.js // module -> rules 에 추가
{
    test: '/\.css$/',
    use: ['vue-style-loader', 'css-loader'] // 앞에꺼가 css를 만들거고 뒤에꺼가 그거를 불러와서 처리해줄거다...?
}
```





번들러: 모듈들을 풀어가지고 app.js로 하나도 번들.. 묶어주는거... 

# 뭔가 이 위로는 뭔말인지 모르겠다. 웹팩 잘모르겠다.. 이걸 대신해주는 무언가.

#  TIL/Vue/newvue

* `npm install -g @vue/cli` 이걸 일단 글로벌에 뭔가 설치를 했고

* vue create {프로젝트이름}  ( 예제로는 vue create too-vue-cli)

  * 뭔가뜨면 엔터! (`default(babel, eslint)`를 사용할거냐?)
    * 익플은 ES6를 지원안해. 그래서 ES6의 애로우 func쓰고 그런거를 ES5로 내려주는게 babel.
  
* 그러고나서 뜨는 파란색 글씨 두줄 쓰면 서버가 짠.

* 그러고 폴더를 확인하면 아까 우리가 위에서 막 했던 설정들이 써있다.
* app.vue를 불러오는 main.js가 있고 app.vue에 가보면 그 서버 띄워주는 뭔가 있다.
* 장고같은 서버를 열어준건가??
* 오타라도 하나라도 생기면 npm run build 그거를 매번!! 해줘야하는데 그럴 필요가 없이 바로바로 보여주는  작업을 한거다.
* 그러고나서 바뀐 것을 실제로 적용시키러면 npm run build를 해주면 된다.
* vue/cli 가 django startproject 같은 느낌...





# 기억속에서..

vue cli를 앞으로 사용할거다

vue 는 싱글파일 컴포넌트를 사용할수있다

그 컴포넌트를 웹 화면에서 보여주려면 어쩔수없이 js환경에서 작성해야하는데

그것을 번들링 하고싶다? 웹팩!

브라우저에서 보여주고싶다!? 웹팩!

vue cli를 쓰게되면 빌드를 따로하지 않아도 서버에서 변경사항을 볼수있고

app.js로 하나로 묶어서 표현이 가능하다.

papage.json은 node 관리, 패키지 설정파일...

바벨같은건- 이런 설정파일때문에 js 쓰기가 어려운데 바벨이 브라우저마다 지원하는 문법이 다른 것을 지난 버전으로 알아서 바꿔주는 역할을 한다.

