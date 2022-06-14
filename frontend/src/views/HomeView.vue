<template>
  <div>
    <section class="py-5 text-center container">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <img class="my-5 py-4" style="width:30rem; height:auto; padding:0; margin:3;" src="@/assets/middle.png" alt="">
          <p class="lead text-muted">Flexmatji와 함께 같은 취향을 가진 사람들과 함께 토론하고,</p>
          <p class="lead text-muted">날짜에 어울리는 영화를 추천받으세요.</p>
          <p class="lead text-muted">관심있는 영화를 모아 관련 영화를 받아볼 수 있습니다.</p>
        </div>
      </div>
    </section>
      <div class="py-5 text-center bg-light">
        <img src="@/assets/inyeongchu.png" alt="">
        <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
              <div v-for="movie in homeMovies" :key="movie.id">
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
                          :to="{ name: 'movie', params: {moviePk: movie.title } }"
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
  computed:{
    ...mapGetters(['homeMovies',])
  },
  methods:{
    ...mapActions(['fetchHome'])
  },
  created() {
    this.fetchHome()
  },
}
</script>

<style scoped>
.card-text {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  word-wrap: break-word;
  text-overflow: ellipsis;
  overflow: hidden;
}
#movieCard{
  padding: 4rem;
}
</style>