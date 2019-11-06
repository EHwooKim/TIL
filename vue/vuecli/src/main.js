import Vue from 'vue' // vue 불러오기
import App from './App.vue' // vue 파일(내가만든) 불러오기

// 새로운 Vue 오브젝트를 만들겠다.
new Vue({
    el: '#app',
    render: function(createElement) {
        return createElement(App)
    }
})