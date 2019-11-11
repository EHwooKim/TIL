<template>
  <li @click="selectedVideo" class="list-group-item my-3 py-3">
    <!-- <iframe width="400" height="300" :src="'https://www.youtube.com/embed/'+video.id.videoId" ></iframe> -->
    <img :src="video.snippet.thumbnails.high.url" :alt="video.snippet.title">
    <h3>{{video.snippet.title}}</h3>
    <p>{{video.snippet.description}}</p>          
  </li>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        video : {
            type: Object,
            required: true
        }
    },
    methods: {
        selectedVideo() {
            // video-select-event 이벤트 발생하여 비디오 리스트로 옮기고 비디오 리스트에서 앱으로 옮기는거 해보자
            // 자식컴포넌트에서는 이벤트 발생(값 전달)
            this.$emit('video-select-event',this.video)
        }
    }
}
</script>

<style scoped> 
/* scoped : 해당 컴포넌트에서만 사용되게 하는 옵션 */
img {
    width: 360px;
}
li {
    cursor: pointer;
}
li:hover {
    background-color: #fffff2;
}
</style>