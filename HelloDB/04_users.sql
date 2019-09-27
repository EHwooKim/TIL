.mode csv
.import users.csv users

-- 1. 나이가 30 이상인 사람의 정보
SELECT * FROM users WHERE age >= 30;
-- 2. 나이가 30 이상인 사람의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 3. 나이가 30 이상이고 성이 김인 사람의 성과 나이만 가져온다면?
SELECT last_name, age FROM users WHERE age >= 30 and last_name='김';
-- 4. 30이상, 김씨 인원수
SELECT COUNT(*) FROM users
WHERE age >= 30 and last_name = '김';
-- 5. 전체 데이터 갯수
SELECT COUNT(*) FROM users;
-- 6. 전체 나이 평균 // SUM, MIN, MAX 등등도 있다
SELECT AVG(age) FROM users;
-- 7. 나이 30이상인 사람들의 평균나이
SELECT AVG(age) FROM users WHERE age >= 30;
-- 8. 계좌 잔액이 가장 높은 사람의 이름과 잔액
SELECT first_name, MAX(balance) FROM users;
-- 9. 30살 이상인 사람들의 계좌 평균 잔액
SELECT AVG(balance) FROM users
WHERE age >= 30;
-- 10. 20대인 사람의 이름 (LIKE 사용)
SELECT * FROM users
WHERE age LIKE '2_';
-- 11. 지역번호가 02인 사람
SELECT * FROM users
WHERE phone LIKE '02-%';
-- 12. 이름이 준으로 끝나는 사람
SELECT * FROM users
WHERE first_name LIKE '%준';
-- 13. 중간번호가 5114인 사람
SELECT * FROM users
WHERE phone LIKE '%-5114-%';
-- 14. 나이 많은 사람 10명
SELECT * FROM users
ORDER BY age DESC LIMIT 10;
-- 15. 나이, 성 순으로 오름차순 10명
SELECT * FROM users
ORDER BY age, last_name ASC LIMIT 10;
-- 16. 나이, 성 순으로 오름차순 10번째 사람
SELECT * FROM users
ORDER BY age, last_name ASC LIMIT 1 OFFSET 9;
