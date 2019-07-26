# Python 

## 00. 💄💄💄 return 값 주의하랍신다!!!💄💄💄

## 01. bool

```python
# True, False 뭐게?
bool('')
bool(' ') 
bool(0)
bool([0])
```

> 정답:
>
> `f,t,f,t`

## 02. 이스케이프 문자열

`\n`, `\t`, `\\`, `\'`, `\"` 이런건 뭔지 알지?

`\r` : 캐리지리턴, `\0`: 널 - 이런것도 있네//

## 03. String interpolation

```python
# 익숙한 f-string, string-format 말고
name = '김태우'
print('Hello, %s' %name) 같은 방법도 있따.
```

## 04. 논리 연산자

`a & b`, `a | b`  => 이것들은 비트 연산자야
python에서는 `and`, `or`, `not`으로 쓰이니까 괜히 위에것도 되겠지 생각 말자

### 단축평가

```python
# 단축평가로 다음 생각해보기
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and [])
print([] and 0)
#-----------
print(3 or 5)
print(3 or 0)
print(0 or 3)
print(0 or [])
print([] or 0)
```

> 정답:
>
> ```text
> 5 0 0 0 []
> -----------
> 3 3 3 [] 0
> ```

### 기타 연산자

* 동일한 object 인지 확인하는 `is`

```python
#1.
a = b = 3
id(a), id(b) 이 둘이 같을까?
#2.
a = b = 257
id(a), id(b) 이 둘이 같을까?
```

> 정답:
>
> 3일 떄는 같지만, 257일 때는 다르다.
>
> 파이썬에서는 -5부터 256까지만 id가 동일하다.

### slicing

`[리스트][이상:미만]`

`'문자'[이상:미만]`

### 연산자 우선 순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자
    \*\*
4. 단항연산자 
    +, - (음수/양수 부호)
5. 산술연산자
    \*, /, %
6. 산술연산자
    +, -
7. 비교연산자, `in`, `is`
8. `not`
9. `and` 
10. `or`

## 05. 기초 형변환

### 암시적 형변환

```python
# boolean 과 integer 더할 수 있을까?
True + 3 결과는?
```

> 정답:
>
> 
>
> True는 강제로 1로 형변환을 하기때문에 계산이 가능하다.
>
> 따라서 답은 4

```python
int(True)  뭐게?
```

> 정답:
>
> 위에서 말했지? 1이라고.

### 명시적 형변환

- string -> intger : 형식에 맞는 숫자만 가능

  ```python
  int('3.5') 안된다고 몇번을 이야기했지?
  int(3.5)는 되는거 당연히 알고 있지? 이 두개 헷갈리지말자
  ```

- `float()` : string, int를 float로 변환 // int -> float 당연히 된다. 긴가민가하지말자

- `str()` : int, float, list, tuple, dictionary를 문자열로 변환//

  - list, tuple, dictionary 들도 문자열로 변환이 된다!!

## 06. 시퀀스 자료형

`리스트`, `튜플`, `레인지`, `문자열`, `바이너리` 는 시퀀스 자료형이다!

`set`이랑 `dictionary`는 아니네? 순서가 없어서 그런가? 그렇네

```python
# 이건 튜플일까요 아닐까요?
('튜플')
```

> 정답:
>
> 아니다.!
>
> 괄호안에 원소(?)가 한개일 때 튜플로 만들고 싶으면
>
> ('튜플',) 과 같이 써줘야 한다.

### 시퀀스 연산자

```python
# 다음 계산 결과는?
a = [1, 2, 3]
a*2
#------
1. [2, 4, 6]
2, [1, 2, 3, 1, 2, 3]
```

> 정답:
>
> 당연히 2번이다.. 혹시나 해서..

## 07. 셋, 딕셔너리

```python
a={}
a는 비어있는 셋? 딕셔너리?
```

> 딕셔너리이다.
>
> 비어있는 셋은 a = set() 으로 만든다.

* 딕셔너리의 `key`로는 불변하는(immutable)한 모든것이 가능하다.
  * immutable : `string`,` integer`,` float`, `boolean`, `tuple`, `range`
* 딕셔너리의 `value`로는 `list`, `dictionary`를 포함한 모든 것이 가능하다.

## 08. 반복문

### 제어문

```python
# 다음 결과는?
for i in range(5):
    if i > 2:
        print('0, 1, 2')
        break
    print(i)
```

### else

* for문에서도 else를 쓸 수 있다.

  `else`문은 끝까지 반복문을 시행한 이후에 실행됩니다.

  (`break`를 통해 중간에 종료되지 않은 경우만 실행)

  ```python
  # 다음 결과는?
  for i in range(5):
      if i > 100:
          break
  else:
      print('살려줘', i)
  ```

  

## 09. 함수

#### 가변 인자, 정의되지 않은 인자, 언패킹

```python
def my_func(*args):
    print(args)
    print(type(args))
    
my_func(1, 2, 3, 4)
#결과는~?
```

* `*` 함수 만들 때, 부를 때, 별 붙이는거 생각 다시 해보자



### 인자 인수

* `인자, 매개변수(parameter)` : 함수를 정의할 때
* `인수(arguments)` : 함수를 호출할 때

### 이름공간

* 변수 탐색하는 순서 - 이거 제대로 알고 있으라신다 💄

>`L`ocal scope : 정의된 함수
>
>`E`nclosed scope : 상위 함수
>
>`G`lobal scope : 함수 밖의 변수 혹은 import된 모듈
>
>`B`uilt-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

```python
print(str(4))
str = 4
print(str(4))
```

* str = 4 이후에 print(str(4))를 하게되면 global scope에서 먼저 찾아 str = 4를 가져오기 때문에 세번째 줄에서 오류가 생긴다.

  우리가 원하는 `str()`은 Built-in scope에 있기 때문이다.

## 10. 문자열 메소드

```python
a = "hI! Everyone, I'm kim"
# 각각 어떻게 될까
print(a.capitalize())
print(a.title())
print(a.swapcase())
```

* `.capitalize()` : 앞글자를 대문자로
* `.title()` : 어포스트로피나 공백을 이후를 대문자로 만들어 반환합니다.
* `.swapcase()` : 대<->소문자로 변경하여 반환합니다.

```python
# 공백
```

* `.replace(old, new[, count])` : count 설정하면 설정값만큼, 안하면 전부

* `lstrip, rstrip, strip[chars]` : 왼쪽, 오른쪽, 양쪽 문자 제거 중간은 못지운다.

* `.index(x)` : x의 첫번째 위치 반환. 없으면 오류 발생 💄

> .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
>
> 4강에 이런것도 있는데 보려면 보든가..

  ### .find(x) .index(x)

```python
# 다음의 결과는 무엇일까요?

'wow'.index('w')
'wow'.index('x')	

'wow'.find('w')
'wow'.find('x')
```

>
>
>정답 : 0, 오류, 0, -1
>
>둘 다 값이 있을 때는 첫번째 위치를 반환
>
>없을 때는 find 는 -1 반환 // index 는 오류발생

## 11. 리스트 메소드

### 값 추가

#### append, 어렵게 값 추가하기

* `append()`는 뭐지 알지

  이거랑 같은 결과지만 어렵게 값을 추가하는 방법

  ```python
  caffe=['스타벅스']
  caffe[len(caffe):] = ['이디야']   
  이래도 추가는 된다네, 리스트로 추가해준거 주의! 그냥 문자열 쓰면 한글자씩 들가
  # 기둥 뒤에 공간 있어요
  caffe[len(caffe):] >>[]
  ```

#### extend 유의점

* `append()` 랑 `extend()`에 리스트 넣을 때 어떻게 다른지 알지?

* 그런데 `append()`, `extend()`에 리스트가 아닌 원소 한개로 넣으면?

  ```python
  caffe=[]
  caffe.extend('블루보틀') #결과가 뭘까요?
  ```

  >
  >
  >정답 : caffe = ['블', '루', '보', '틀']
  >
  >그러니 조심할것
  
* .extend() 역시 return 값은 None 입니다!!!!!!💄💄💄💄

  ```python
  a=['안', '녕']
  print(a.extend(['하', '세', '요']))
  
  # 이거 결과 난 당연히 안녕하세요인줄 알았지
  ```

  

#### 원하는 위치에 값 넣기

* 원하는 `위치`에 값을 넣고 싶을 떄는 .insert(i, x) 

### 값 삭제

#### remove(x)

```python
x=[1, 1, 2, 3, 4]
print(x.remove(1))
print(x)
# 두개의 print결과는?
```

>
>
>정답 : 
>
>None
>
>[1, 2, 3, 4]
>
>리턴값은 None,  원본 리스트를 바꿔준다.
>
>x 전부 없애주는게 아니다아, 인덱스가 아닌 값을 업애주는거다아

* `remove(x)`: 리스트에서 값이 x인 것을 찾아 앞에서 부터 **한번** 만 없애준다, 없으면 오류!

#### .pop(i)

```python
x=[1, 2, 3, 4, 5]

print(x.pop(3))
print(x)
# 두개의 print 결과는?
```

>
>
>정답 :
>
>4
>
>[1, 2, 3, 5]
>
>pop(x): x값을 업애주는게 아니라 인덱스가 x인 값을 없애주고 그 값을 리턴한다.
>
>x 인덱스가 아니라 x 값을 없애주는 거면 굳이 리턴값으로 없앤 값을 보여줄 필요가 없겠지

* `pop(i)` : 리스트에서 **인덱스가 i인** 값을 없애준다.

  ​				**i를 넣지 않으면** `마지막 값`을 없애준다. 없으면 오류

#### .clear()

* `.clear()` : 리스트의 `모든` 항목 삭제

### 탐색 및 정렬

#### .index(x)

* `index(x)` : 원하는 x 값의 인덱스를 알려주고 없을 경우 오류.

  ​					  찾는 값이 없을 경우 -1 돌려주는 `.find()!` 하지만 그건 리스트에는 없다네 문자열로 가시게나

#### .sort()

* sort()와 sorted() 차이가 뭐게? 

```python
x=[3,5,1,2,3,1]
x = x.sort()
x.extend([8,5,1])
x = sorted(x)
print(x)

# 어디가 불편하십니까? 왜 불편하고 어떻게해야 편안해질까요?

x=['6', '8', '5', '1', '2', '3']
print(''.join(_______))

# 정렬된 문자열을 만들고 싶다면 빈칸에 어떤 표현이 맞을까요?
```

>
>
>sort()는 원본을 바꿔주고 return 값이 None이기 때문에 x = x.sort()와 같이 쓰면 x에 None이 가버려
>
>sorted()는 원본은 냅두고 return값이 정렬값이라  변수에 넣어주지 않으면 결국 정렬값을 얻지 못해

#### .reverse()

* `reverse()` : **정렬 없이** 순서만 뒤집어 준다.
* `reversed()` , `.reverse()` 의  차이는 `sorted()` , `.sort()` 랑 같아

### 복사

* 그거 리스트, 딕셔너리 같은 것들은 변수에 값이 저장되는게 아니라 주소가 저장되는거라서 복사 후 값변경하면 원본도 같이 변한다는 그 이야기.

  Day4 문서 다시 한번 봐보자.

  ```python
  #전체적으로 한번 더 보고 이거는 한번 더 생각해보자.
  a = [1, 2, [1, 2]]
  b = a[:]
  b[2] = [0, 3]
  print(a, b)
  # 결과가 뭐게? 이유는?
  ```
  
  >
  >
  >정답:
  >
  >[1, 2, [1, 2]] [1, 2, [0, 3]]
  >
  >이유는
  >
  >a = [1, 2, 3]
  >b = a
  >b = [3]
  >print(a, b) 의 결과가
  >
  >[1, 2, 3], [3] 인거랑 같아.

### 12. 딕셔너리 메소드

* 딕셔너리는 순서가 없으니 인덱스로의 접근이 안됩니다.
* 그렇기 때문에 메소드를 사용할 때 `key`를 통한 접근을 합니다.

#### .update()

* 주의할점이 있어

  ```python
  # 다음 중 함정을 고르시오
  my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
  
  my_dict.update(apple ='사과입니다')  
  my_dict.update('banana':'바나나지롱')
  my_dict.update(grape='포도')
  
  ```

  >
  >
  >두번째 줄이 틀렸다아.
  >
  >저렇게 쓰고 싶으면 당연히 양쪽에 중괄호가 필요하겠지  
  >
  >my_dict.update({}'banana':'바나나지롱'}) 이렇게 말이야.. 생각해보면 당연한거지

#### .pop(key[, default])

* `pop(key[,default])` : 해당 `key`와 `value`를 삭제해주고

  `return` 값으로 그 `value` 를 반환합니다.

* `[, default]`로 초기값 설정이 가능합니다. 해당 `key`가 없을 때 초기값이 반환되며 

* 초기값을 설정하지 않고, 없는 `key`를 `pop()`하면 `KeyError`가 발생합니다.`None`이 아니구요💄

#### .get(key[,default])

* `get(keyp,default])` : `key`를 통해 `value`를 가져옵니다. 
* `default`로 `None`이 설정되어 있기에 `KeyError`가 발생하지 않습니다💄

### 13. 세트 메소드

#### 값 추가하는 두가지 방법

* `.add(elem)` : 값 추가!

* `.update(*others)` : 값 여러개 추가!

  ```python
  a = {"사과", "바나나", "수박"}
  a.update('토마토', '딸기')
  print(a)
  
# 결과는~?
  ```
  
  >
  >
  >이렇게 쓰는게 아닙니다!!!!!!!!!!!!!!!!!
  >
  >세트에서 `update`로 값 여러개 추가 하려면 꼭 iterable 한 값을 넣어줘야 합니다.
  >
  >위의 결과는 아래와 같습니다
  >
  >```
>{'수박', '사과', '토', '기', '바나나', '딸', '마'}
  >```
  
  ```python
  a = {"사과", "바나나", "수박"}
  a.update(('토마토', '딸기'))
print(a)
  ```

  > 위의 방법이  올바른 방법입니다.
  
  ```python
  a = {"사과", "바나나", "수박"}
  a.update(('토마토'), ('딸기')) 
  print(a)
  
#그럼 이건 될까?
  ```
  
  > 안된다고 합니다..
  >
  > a.update(('토마토',), ('딸기',))  이렇게 해야합니다.

#### 값을 삭제하는 세가지 방법

* `.remove(elem)` : 세트에서 `elem`을 삭제하고 없으면?? `KeyError`

* `.discard(elem)` : `elem`을 삭제하고 없으면??? 에러 방생안합니다. `.get()`처럼 `default`값 설정은 못합니다.

* `.pop()` :`임의의 원소`를 제거하고 return 합니다.

  > 순서, 키 둘 다 없으니 당연히 임의의 원소를 제거하겠지// list.pop() 이랑 헷갈리지 말자. 


### 12. map(), zip(), filter()

* map()

  ```python
  # 때에 따라서 map을 쓰면 이렇게 코드가 간단해진다.
  print(''.join(map(str, a)))
  ```

* zip(*iterables)

  ```python
  print(list(zip(girls, boys)))
  #이거하면 각 원소 짝지어서 나오는 그거.
  ```

  * iterable인 것은 다 되니까 문자열도 사용가능하고

  * 길이가 짧은 것을 기준으로! 구성한다!💄

    (길이 긴 것을 기준으로도 가능은 한데.. 의미읎어 안써)

### 13. OOP

그냥 필기 전체를 보도록.







​









* 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range







```python
a[-1]
a[:-1]
a[::-1]
# 이 것들의 결과를 아느냐
a=[0, 1, 2, 3, 4, 5, 6, 7]
print(a[:-3])
# 결과가 무엇인지 아느냐
```

>
>
>마지막 것만 가져오기
>
>마지막 것만 빼고 가져오기
>
>무적의 뒤집개
>
>[0, 1, 2, 3, 4]  
>
>슬라이싱 할 때 해당 인덱스 미만까지인거는 당연히 동일하다



안나온다 모듈 에러 상속