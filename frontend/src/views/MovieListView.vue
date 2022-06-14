<template>
  <div>
    <section class="py-5 text-center container">
      <img style="width:auto; height:100%" src="@/assets/오영.png" alt="">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <p class="lead text-muted">날짜에 어울리는 영화를 추천받으세요.</p>
        </div>
      </div>
    </section>
      <div class="py-5 bg-light">
        <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
              <div v-for="movie in movies" :key="movie.id">
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
                          :to="{ name: 'movie', params: { moviePk: movie.title } }"
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
  name: 'MovieList',
  computed: {
    ...mapGetters(['movies',])
  },
  methods: {
    ...mapActions(['fetchMovies'])
  },
  created() {
    this.fetchMovies()
    console.log(this.movies)
  },
}
</script>

<style scoped>
img {
  height: 3rem;
}
</style>