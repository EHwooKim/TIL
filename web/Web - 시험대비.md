# Web

## HTML

* `HTML` : Hyper Text Markup Language

### semantic tag, tag

* `header`, `nav`, `section`, `article`, `aside`, `footer` 

  > HTML5에서 추가된 시멘틱태그들

  `div`도 시멘틱이야?

* `b`,` strong` 태그 : 둘 다 볼드체 이지만 `strong`은 시멘틱 태그. 

* `i`, `em` 태그 : 둘 다 이탤릭체 이지만, `em`은 시멘틱 태그

* `mark` 태그 : 하이라이팅
* `pre` 태그 :  마크다운에서 ```와 같은 효과. 공백, 엔터 다 그대로 적용된다.



* `링크, 경로` 걸기
  * `src` : `img`태그에서 이미지 경로 (로컬 / 웹)
  * `href`  : `a` 태그에서 가고자하는 위치(?) 경로 (웹주소, id 등..)

* table, form..!

## CSS

### 크기단위

* `em` : 배수 단위로 상대 단위이다. 요소에 지정된 사이즈 (상속,디폴트 사이즈)에 상대적인 사이즈를 설정. 상속에 따라 기준이 바뀐다
* `rem` : 최상위 요소(html)의 사이즈를 기준으로 삼는다.

### 색상

* `HEX` : #ffffff
* `RGB` : rgb(0,0,0)  
* `RGBA` : rgba(0, 0, 0, 0,5)  투명도추가

### 박스모델

* shorthand : 상하/좌우 . 상/좌우/하 . 시/계/방/향

### display

* `block` : 화면 크기 전체의 가로폭 차지.(width : 100%) 너비가 정해지면 나머지를 `margin`으로

  * `div`, `h1~h2`, `p`p, `ol`, `ul`, `li`, `hr`, `table`, `form`

* `inline` : content의 너비만큼 가로폭 차지. `width`, `height`, `margin-top`, `margin-bottom` 프로퍼티 지정 못한다.  상하 여백은 `line-height`로 지정.`

  * `span`, `a`, `strong`, `img`, `br`, `input`, `select`, `textarea`, `button`

* `inline-block` : `block`, `inline` 요소 특징을 모두 가진다.

  `inline`처럼 한 줄에 표시 되면서 . `width`, `height`, `margin-top`, `margin-bottom` 지정 가능.

* `Nono` : 화면에 표시되지 않으며 **공간조차 사라진다** :warning:

### visibility 

* `visible` : 기본값, 해당 요소를 보이게
* `hidden` :  해당 요소를 안보이게 **공간은 남아있다**:warning:

### position

* `static` : 기본 배치

* `relative` : 기본 위치를 기본으로 좌표 프로퍼티를 사용하여 위치이동 가능.(음수도 가능)

* `absolute` : 부모요소, 가능 가까운 조상요소를 기준으로 좌표 만큼 이동. (`static`은 제외)

  `relative`, `absolute`, `fixed`가 선언된 부모, 조상을 기준으로  위치 결정

* `fixed` :  부모 요소와 관계없이 `viewpoint`를 기준으로 위치이동. 스크롤 되어도 고정

### background

* 이미지크기 :`width`, `height` 순으로 지정.

  값 하나만 지정하면 `width` 지정 + `height` : `auto`

* `cover` :  w, h 중 큰 값에 맞춤. 보이지 않는 영역 발생
* `contain` : 보이지 않는 영역이 없도록 조정

## bootstrap

### spacing

* `mt-n5` : 음수값도 지정 가능

### Grid

| -            | Extra small | Small    | Medium   | Large    | Extra Large |
| ------------ | ----------- | -------- | -------- | -------- | ----------- |
| width        | < 576px     | >= 576px | >= 768px | >=992px  | >= 1200px   |
| class prefix | .col-       | .col-sm. | .col-md- | .col-lg- | .col-xl-    |

