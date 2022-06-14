<template>
  <div>
    <section class="py-2 container">
      <div class="row py-lg-5 text-center">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h3 class="fw-light "><b>{{movie.title}}</b></h3>
          <p class="lead text-muted">개봉일: {{movie.release_date}} |
              평점: {{movie.vote_average}}
          </p>
          <span class="lead text-muted">장르 :  </span>
          <span v-for="genre in movie.genres" :key="genre.pk" class="lead text-muted">
            <span>{{genre.name}}  </span>
          </span>
        </div>
      </div>
    <div class="card-all card mb-3 border-secondary mb-3 text-center" style="max-width: 1200px;">
      <div class="row g-0">
        <div class="col-md-4">
          <img :src='`https://www.themoviedb.org/t/p/original/${movie.poster_path}`'
            style="height: 570px; width:auto; min-width: 140px;"
            alt="...">

          <button class="my-3 mx-5 btn"  @click="likeMovie(movie.id)">
            <i class="fa-solid fa-heart" style="color:crimson;">{{likeCount}}</i>
          </button>

        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title my-3"><b>줄거리</b></h5>
            <p class="card-text">{{movie.overview}}</p>

            <h5><b>영화 예고편</b></h5>
            <iframe :src="`https://www.youtube.com/embed/${movie.youtube_key}`" frameborder="0" width="560" height="315"></iframe>
          </div>
        </div>
      </div>
    </div>
      <!-- <span v-for="user in movie.like_users" :key="user.username" 
        :v-if="user.username === currentUser.username">
        <button  @click="likeMovie(movie.id)">
          찜하기!
        </button>
      </span>
      <span :v-else> 
        <button @click="likeMovie(movie.id)">
          내가 찜한 목록에서 제외
        </button>
      </span> -->
    <hr>
    <movie-comment-list :movieComments="movie.movie_comments"></movie-comment-list>

    </section>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieCommentList from '@/components/MovieCommentList.vue'

export default {
  name: 'MovieDetail',
  components:{ MovieCommentList },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser']),
    likeCount() {
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie',])
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style scoped>
h3 {
  margin: 1rem;
}
.card-all{
  width: 1200px;
  margin:0 auto;
}
</style>