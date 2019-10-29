console.log('Happy!')

// var
console.log(a)  // undefined
var a = '변수'
// var는 변수 hoisting(호이스팅)을 한다.
// : 변수의 선언을 해당 스코프 범위 내에서 최상단에 "선언"을 함.
// 즉, var는 js가 다음과 같이 이해하고 실행한다.
// var a
// console.log(a)
// a = '변수'


// let  (ES6+)
// 재선언 불가. 재할당 가능
console.log(b)  // Reference error
let b = '변수'

let b = '다른 변수' // 재선언 불가능
b = '다른변수' // 재할당 가능


// const  (ES6+)
// 재할당 및 재선언이 불가능하다!
// 재할당이 안되니까 const tak 같이 선언만 하는 것이 불가능하다. 선언, 할당 동시에 이루어져야.
const c = '상수' 
c = '다른 상수'  // Uncaught TypeError: Assignment to constant variable
const c = '또 다른 상수' // Uncaught SyntaxError: Identifier 'c' has already been declared error


// let, const vs. var
// 재선언이 불가능하다 vs. 가능하다
// 블록 스코프 vs. 함수 스코프 

var outerVar = '밖'
if (true) {
    var outerVar = '안'
    console.log(outerVar)  // 안
}
console.log(outerVar)   // 안


let outerLet = '밖'
if (true) {
    let outerLet = '안'
    console.log(outerLet)  // 안
}
console.log(outerLet)  // 밖

