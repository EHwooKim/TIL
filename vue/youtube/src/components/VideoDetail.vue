<template>
  <!-- 비디오가 있을 때만 보이게 조건식 -->
  <div v-if="video"> 
    <iframe width="560" height="315" :src="videoUrl" frameborder="0" allow="autoplay" allowfullscreen></iframe>
  </div>    
</template>

<script>
export default {
    name: 'VideoDetail',
    props: {
        video: {
            type: Object,
            // required: true 초기에 선택이 되어있지 않을 수 있으므로  
        }
    },
    computed: {
        videoUrl() {
            return `https://www.youtube.com/embed/${this.video.id.videoId}`
        }
    }
}
</script>

<style>

</style>