-- DDL(데이터 정의 언어)
-- 관계형데이터베이스 구조를 정의하기 위한 명령어
-- CREATE ALTER DROP
-- 테이블 생성
CREATE TABLE classmates (
    id  INTEGER PRIMARY KEY,
    name TEXT
);
-- 테이블 목록 조회
.tables

-- 테이블 스키마 조회
.schema classmates

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블 명 변경
ALTER TABLE articles RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL;
-- 이러면 NOT NULL 조건 때문에 오류가 뜨는데
-- 해결법 1. NOT NULL 삭제
-- 해결법 2. DEFAULT 1;과 같이 default값 설정.