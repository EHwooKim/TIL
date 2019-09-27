CREATE TABLE classmates (
    name TEXT, 
    age INT,
    address TEXT
);
-- DATA 추가
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

-- 모든 열의 데이터를 넣을 때는 컬럼을 명시할 필요가 없다!
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
-- 여러 데이터 넣기
INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('홍순범', 27, '대전');

-- 따로 PK를 설정 안해도  row id가 자동으로 생성되어 pk로 사용가능하고
-- pk 설정하면 pk가 rowid를 대신한다.
SELECT rowid, * FROM classmates;

-- 비어있는 값을 허용하지 않는다. NOT NULL
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL);

-- LIMIT : 몇개 가져올지
SELECT rowid, name FROM classmates LIMIT 1;
-- OFFSET : 몇칸 띄고나서 가져올지
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 1;

-- WHERE column=value : 특정 조건에 맞는 값을 가져오기
SELECT * FROM classmates 
WHERE address='대전';

-- DISTINCT :  특정 column 중복제거
SELECT DISTINCT age FROM classmates;

-- DELETE: 삭제. 삭제는 중복값이 없는 pk로 하는게 좋겠지
DELETE FROM classmates WHERE rowid=4;

-- 마지막 데이터를 삭제하고 새롭게 추가해보면,
-- 삭제된 id가 다시 활용되는 것을 볼 수 있다.
-- 이를 방지하기 위한 것이 바로!
-- AUTOINCREMENT: rowid처럼 앞의 값이 지워져도 그 값을 채우는게 아닌 뒤쪽으로 이어서 값이 생성되도록
CREATE TABLE tests (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name NEXT NOT NULL);

-- UPDATE: 값 수정
UPDATE calssmates SET age=30, address='대전' WHERE name='홍순범';


-- column 한개를 추가 할때는 ADD COLUMN 하면되지만 이미 있는 COLUMN의 옵션을 바꿀때는 밑에처럼
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
ALTER TABLE friends RENAME TO tmp;
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location VARCHAR(100) NOT NULL
);
INSERT INTO friends SELECT * FROM tmp;
DROP TABLE tmp;
