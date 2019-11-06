<template>
    <div>
        <h1>이게 싱글파일컴포넌트, 최상의 컴포넌트입니다.</h1>
        <TodoList category="취업"></TodoList>
        <TodoList category="수업"></TodoList>
        <TodoList category="개인"></TodoList>
    </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
    components: {
        TodoList
    }
}
</script>

<style lang="">
    
</style>