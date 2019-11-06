<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <TodoList category="싸피"/>
    <TodoList category="취업"/>
    <TodoList category="개인"/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue' // HelloWorld.vue 였던것을 변경

export default {
  name: 'app',
  components: {
    TodoList //HelloWorld 였던것을 이렇게 변경
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
