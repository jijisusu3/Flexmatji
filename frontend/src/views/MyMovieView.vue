<template>
  <div>
    <section class="py-5 text-center container">
      <div class="row">
        <div class="col-lg-6 col-md-8 mx-auto">
          <img style="width:100%; height:auto;" src="@/assets/내가좋아하는영화.png" alt="">
          <p class="lead text-muted">좋아하는 영화를 관리하고, Detail 을 볼 수 있습니다.</p>
          <p class="lead text-muted">이 정보를 기반으로 Flixmatji가 영화를 추천해 드립니다.</p>
        </div>
      </div>
    </section>
    <div class="py-5 bg-light">
      <div class="container">
        <div class="text-center">
          <h3>
            추천 영화
          </h3>
        </div>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
            <div v-for="recommendMovie in recommendMovies" :key="recommendMovie.id">
              <div id="movieCard" class="col-5">
                <div class="card" style="width: 15rem;">
                  <router-link 
                    :to="{ name: 'movie', params: {moviePk: recommendMovie.title} }"
                  >
                    <img class="card-img-top" style="height: 100%; width: 100%;" :src='`https://www.themoviedb.org/t/p/original/${recommendMovie.poster_path}`'>
                  </router-link>
                  <div class="card-body">
                    <p class="card-text"><b>{{recommendMovie.title}}</b></p>
                    <p class="card-text">{{recommendMovie.overview}}</p>
                    <div class="d-flex justify-content-between align-items-center">
                      <router-link 
                        :to="{ name: 'movie', params: {moviePk: recommendMovie.title} }"
                      >
                        <button type="button" class="btn btn-sm btn-outline-secondary">영화 상세 페이지로</button>
                      </router-link>
                      <small class="text-muted">평점: {{recommendMovie.vote_average}}</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>

        </div>
      </div>
    </div>

    <div class="py-5 bg-light">
      <div class="container">
        <div class="text-center">
          <h3>
            당신이 찜한 영화
          </h3>
        </div>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
            <div v-for="movie in myMovie.like_movie" :key="movie.id">
              <div id="movieCard" class="col-5">
                <div class="card" style="width: 15rem;">
                  <router-link 
                    :to="{ name: 'movie', params: {moviePk: movie.title} }"
                  >
                    <img class="card-img-top" style="height: 100%; width: 100%;" :src='`https://www.themoviedb.org/t/p/original/${movie.poster_path}`'>
                  </router-link>
                  <div class="card-body">
                    <p class="card-text"><b>{{movie.title}}</b></p>
                    <p class="card-text">{{movie.overview}}</p>
                    <div class="d-flex justify-content-between align-items-center">
                      <router-link 
                        :to="{ name: 'movie', params: {moviePk: movie.title} }"
                      >
                        <button type="button" class="btn btn-sm btn-outline-secondary">영화 상세 페이지로</button>
                      </router-link>
                      <small class="text-muted">평점: {{movie.vote_average}}</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MyMovieView',
  data(){
    return {
      username: this.$route.params.username,
    }
  },
  computed:{
    ...mapGetters(['myMovie', 'currentUser', 'recommendMovies']),
  },
  methods:{
    ...mapActions(['fetchMyMovie', 'fetchRecommendMovies'])
  },
  created(){
    const payload = { username: this.username}
    this.fetchMyMovie(payload)
    this.fetchRecommendMovies()
    console.log(this.recommendMovies)
  }
}
</script>

<style scope>
.card-text {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  word-wrap: break-word;
  text-overflow: ellipsis;
  overflow: hidden;
}
#movieCard{
  padding: 4rem;
}
@keyframes ldio-a6fmloew0ot {
  0% { opacity: 1 }
  100% { opacity: 0 }
}
.ldio-a6fmloew0ot div {
  left: 94px;
  top: 48px;
  position: absolute;
  animation: ldio-a6fmloew0ot linear 1.4492753623188404s infinite;
  background: #e771fe;
  width: 12px;
  height: 24px;
  border-radius: 6px / 12px;
  transform-origin: 6px 52px;
}.ldio-a6fmloew0ot div:nth-child(1) {
  transform: rotate(0deg);
  animation-delay: -1.328502415458937s;
  background: #e771fe;
}.ldio-a6fmloew0ot div:nth-child(2) {
  transform: rotate(30deg);
  animation-delay: -1.2077294685990336s;
  background: #e6cfc9;
}.ldio-a6fmloew0ot div:nth-child(3) {
  transform: rotate(60deg);
  animation-delay: -1.0869565217391304s;
  background: #e16af8;
}.ldio-a6fmloew0ot div:nth-child(4) {
  transform: rotate(90deg);
  animation-delay: -0.9661835748792269s;
  background: #d7e0c2;
}.ldio-a6fmloew0ot div:nth-child(5) {
  transform: rotate(120deg);
  animation-delay: -0.8454106280193235s;
  background: #ebcde2;
}.ldio-a6fmloew0ot div:nth-child(6) {
  transform: rotate(150deg);
  animation-delay: -0.7246376811594202s;
  background: #d97ef9;
}.ldio-a6fmloew0ot div:nth-child(7) {
  transform: rotate(180deg);
  animation-delay: -0.6038647342995168s;
  background: #e1ebc6;
}.ldio-a6fmloew0ot div:nth-child(8) {
  transform: rotate(210deg);
  animation-delay: -0.48309178743961345s;
  background: #de81f5;
}.ldio-a6fmloew0ot div:nth-child(9) {
  transform: rotate(240deg);
  animation-delay: -0.3623188405797101s;
  background: #e771fe;
}.ldio-a6fmloew0ot div:nth-child(10) {
  transform: rotate(270deg);
  animation-delay: -0.24154589371980673s;
  background: #e6cfc9;
}.ldio-a6fmloew0ot div:nth-child(11) {
  transform: rotate(300deg);
  animation-delay: -0.12077294685990336s;
  background: #e16af8;
}.ldio-a6fmloew0ot div:nth-child(12) {
  transform: rotate(330deg);
  animation-delay: 0s;
  background: #d7e0c2;
}
.loadingio-spinner-spinner-kgux2dq1oj8 {
  width: 200px;
  height: 200px;
  display: inline-block;
  overflow: hidden;
  background: #f8f9fa;
}
.ldio-a6fmloew0ot {
  width: 100%;
  height: 100%;
  position: relative;
  transform: translateZ(0) scale(1);
  backface-visibility: hidden;
  transform-origin: 0 0; /* see note above */
}
.ldio-a6fmloew0ot div { box-sizing: content-box; }
/* generated by https://loading.io/ */
</style>