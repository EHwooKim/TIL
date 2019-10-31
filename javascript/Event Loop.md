* `11_blocking.js` 랑 같이 잘 보자..

* 이벤트 루프 : `call stack`, `callback queue` 확인하는 역할
  * `call stack`이 비어있으면, `callback queue`에서 `call stack`으로 이동.
  * 이벤트(함수실행..)
  * tick(틱)
  
* synchronous / Asynchronous   (동기 / 비동기)

  *  **Synchronous/Asynchronous는 호출되는 함수의 작업 완료 여부를 누가 신경쓰냐가 관심사**다. 

  * 호출되는 함수에게 callback을 전달해서, 호출되는 함수의 작업이 완료되면 호출되는 함수가 전달받은 callback을 실행하고, 호출하는 함수는 작업 완료 여부를 신경쓰지 않으면 Asynchronous다. 

  *  호출하는 함수가 호출되는 함수의 작업 완료 후 리턴을 기다리거나, 또는 호출되는 함수로부터 바로 리턴 받더라도 작업 완료 여부를 호출하는 함수 스스로 계속 확인하며 신경쓰면 Synchronous다. 

    

* blocking / non-blocking

  * **Blocking/NonBlocking은 호출되는 함수가 바로 리턴하느냐 마느냐가 관심사**다.
  * 호출된 함수가 바로 리턴해서 호출한 함수에게 제어권을 넘겨주고, 호출한 함수가 다른 일을 할 수 있는 기회를 줄 수 있으면 NonBlocking이다. 
  * 그렇지 않고 호출된 함수가 자신의 작업을 모두 마칠 때까지 호출한 함수에게 제어권을 넘겨주지 않고 대기하게 만든다면 Blocking이다. 
