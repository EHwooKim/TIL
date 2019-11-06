<template>
    <div class="todo-list">
        <h2> {{ category }} </h2>    
        <input v-model="newTodo" type="text"> 
        <button @click="addTodo">추가</button><br>
        <li v-for="todo in todos" :key="todo.id">
            {{ todo.content }}
            <button @click="removeTodo(todo.id)">삭제</button>
        </li>
    </div>
</template>
<script>
export default {
    props: {
        category: {
            type: String,
            required: true
            }
        },
        // 이 component에서 사용할 data. object를 담았던 이전과 다르게 func을 담고 object를 return. 호출할 때마다 새롭게 return하니까 각각 보게되는거지.(?)
        data: function() { 
            return {
            todos: [],
            newTodo: '',
            }
        },
        methods: {
            addTodo() {
            this.todos.push({
                id: Date.now(),
                content: this.newTodo
            })
            this.newTodo = ''
            },
            removeTodo(removeTodoId) {
            this.todos = this.todos.filter( todo => {
                return removeTodoId !== todo.id
            })
            }
        }
    }
</script>


<style lang="">
    /* li {
        color: blue;
    }
     */
</style>