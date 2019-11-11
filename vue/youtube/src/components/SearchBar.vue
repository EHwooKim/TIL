<template>
    <div>
        <form action="">
            <h1>유튜브 검색기</h1>
            <input @change="onInput" type="text">
            <!-- <button type="submit"><i class="fas fa-search"></i></button> -->
        </form>
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            console.log('==search bar==')
            console.log(event.target.value) // console을 못쓰게 하려는 오류메세지 뜨는데 개발중에는 필요하니 pakage.json에 옵션추가했다.
            // $emit(이벤트이름, 값) : Custom Event 발생  (click 등의 이벤트가 아닌 내가 만든 이벤트)
            // 이벤트이름의 이벤트를 발생!!! 시킴(트리거) 그렇게 해서 부모에게 값을 넘겨주는거지
            this.$emit('input-change-event', event.target.value)
        }
    }
}
</script>

<style>

    
</style>