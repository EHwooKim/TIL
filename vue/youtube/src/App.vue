<template>
  <div id="app">
    <div class="container">
      <search-bar @input-change-event="onInputChage"></search-bar>
      <video-detail :video="finallySelectedVideo"></video-detail>
      <video-list @video-select-event="selectedVideo" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'app',
  components: {
    SearchBar,
    VideoList,
    VideoDetail
  },
  // SFC 컴포넌트에서 data는 오브젝트를 리턴하는 함수로 표현한다.
  data() { 
    return{
    videos: [],
    finallySelectedVideo: null
    }
  },
  methods: {
    selectedVideo(video) {
      console.log('앱도착')
      this.finallySelectedVideo = video
      console.log(this.finallySelectedVideo)
    },
    onInputChage(value) {
      console.log('==app==')
      console.log(value)
      axios.get('https://www.googleapis.com/youtube/v3/search', {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: value,  // 검색어는? 넘어오는 value겠지?
        }
      })
      .then(response => {
        console.log(response)
        this.videos = response.data.items
      })
      . catch(error => {
        console.log(error)
      }) 
    }
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
