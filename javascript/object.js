// object 만드는 방법
const me = {
    name:'tak',
    phone: '010-9429-7950',
    // 메서드에서 arrow func 사용 금지인기 알지!?!?!?!?!?
    // this 가 window로 가버리기 때문에.
    greeting: function() {
        return 'hi' + this.name
    }
}
// 지금까지 이렇게 객체로 만들어왔지

// 함수선언으로 우리가 익숙한 형태의 object 생성 가능
// 인자를 받아서 뭔가를 하는, 다양한 객체를 만들고 싶을 때.
// 다음과 같이 함수로 만들어 놓고 ''new'' 키워드로 불러와 객체 생성가능.
const Person = function(name, phone) {
    this.name = name
    this.phone = phone
    this.greeting = function() {
        return 'hi' + this.name
    }
}
const lee = new Person('이경호', '010-2020-0202') // new! 특정한 오브젝트를 만드는 키워드
lee.name
lee.greeting()

// 그럼 arrow func 으로도 될까?
const Animal = name => {
    this.name = name
}
const dog = new Animal('dog') // Error!!!!!!!!!
// 생성자 함수에서는 arrow func 사용 금지


// object 리터럴
const name = '겨레'
const phone = '010-0000-2222'
const greeting = function () {
    return 'hi,' + this.name
}
const you = {
    name,
    phone,
    greeting
}
//이런식으로 쓰는게 오브젝트 리터럴 방법. 축약형이다 라고 간단히 생각하면 된다.