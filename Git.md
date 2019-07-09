# Git 

` Git`은 `분산형 버전관리스세템(DVCS)`이다.

* Window에서 `Git`을 사용하기 위해서는 `Git bash`를 반드시 설치해야 함.

* 참고자료
* [Git Scm](https://git-scm.com/book/ko/v2) //*대괄호로 문자, 소괄호로 링크
* [누구나 쉽게 이해할 수 있는 Git](https://backlog.com/git-tutorial/kr/)

## Git 기본 명령어(로컬)

* 로컬에서 처음 Git을 활용하는 경우 아래의 설정을 해줘야 한다.

  ```bash
  $ git config --global user.name 'EHwooKim'
  $ git config --global user.email 'ehwoo0707@naver.com'
  ```

  커밋하는 사람(`author`)이 누구인지 설정! 

  Github email이랑 다르면, Github에서 다른 사람이 커밋한 것으로 인식됨!

  *컴퓨터에서 한번만 설정해주면 된다.*  //*한개로 감싸면 *이탤릭체*, *두개로 감싸면 **굵은거**



1. Git 저장소 설정

   ```bash
   $ git init #라고 치면 다음과 같은 결과
   Initialized empty Git repository in C:/Users/student/Desktop/thing/.git/
   
   student@DESKTOP MINGW64 ~/Desktop/thing (master)
   ```

   * `git init`명령어를 입력하면, 해당 디렉토리에 `.git/`폴더가 생성된다.(숨김폴더) 
   * 모든 git과 관련된 내용은 해당 폴더에 담겨있다.
   * 저장소로 설정되었다면, `git bash`에서 `master`가 나타난다. (중요)

2. Staging area(커밋 대상 목록)에 담기

   ```bash
   $ git add . (현재 디렉토리 모든 것)
   $ git add a.txt (예시)
   $ add Start_camp (폴더 안 모든 파일)
   ```

   * `git add` 명령어를 통해 특정 파일 혹은 폴더를 `commit` 할 목록(`staging area`,`INDEX`)에 담아 놓는다.

   * 반드시 `git status` 명령어를 통해 내가 원하는 파일이 반영되었는지 확인한다.

     ```bash
     $ git status
     ...
     Changes to be committed:
       (use "git reset HEAD <file>..." to unstage)
     
             new file:   test.txt
     ```

3. 이력 남기기(`commit`)

   ```bash
   $ git commit -m '커밋메시지'
   [master 8d18062] test중입니다
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```

   * `commit`은 현재 소스코드의 상태를 **스냅샷** 찍는 것과 동일하다.

   * `Staging Area`에 담겨 있는 내용을 이력으로 남긴다.

   * 커밋메시지는 반드시 해당 이력의 내용을 정확하게 표현해야 한다.

     (보통 오픈소스프로젝트, 회사 내에서 관련된 컨벤션이 존재함.)

4. 커밋이력 확인하기

   ```bash
   $ git log
   commit 8d1806262765eba802fd309c645c7268b37d4af1 (HEAD -> master)
   Author: EHwooKim <ehwoo0707@naver.com>
   Date:   Tue Jul 9 10:49:07 2019 +0900
   
       test중입니다
   ```

   * `git log -n` 옵션을 주면, 최근 n개의 커밋을 보여준다.
   * 커밋 이력을 남긴 이후에 커밋 메시지 변경, 삭제 등을 할 수 있는데 이 경우는 매우 조심해야 한다.

5. **git 상태 확인**

   **항상 모든 명령어를 입력하기 전에 아래의 명령어를 입력하는 습관을 들이자!**

   ```bash
   $ git status
   ```



## Git 원격 저장소 활용하기

원격 저장소(`remote repository`)는 `github`, `gitlab`, `bitbucker` 등 다양한 서비스를 활용할 수 있다.

1. 원격 저장소(`remote repository`) 설정

   ```bash
   $ git remote add origin __http://github.com__
   ```

   * 로컬 저장소에 최초에 한번만 등록하면 된다.
   * `원격 저장소(remote)` 를 `origin` 이라는 이름으로 정해진 url을 `등록(add)` 하는 것이다.
   * 어떤 저장소를 가졌는지(?)는 `git remote -v` 로 확인

2. 원격 저장소로 `push`

   ```bash
   $git push origin master
   ```

   * `origin` 으로 설정된 원격 저장소에 `push` 한다.
   
3. 원격 저장소에서 `pull`

   ```bash
   $ git pull origin master
   ```

   * 원격 저장소에 새로운 변경 사항이 있는 경우 `pull` 을 통해 받아온다.

4. `clone`

   ```bash
   $ git clone __url__
   ```

   * `clone` 은 원격 저장소에서 최초에 받아올 때 활용한다.
   * 