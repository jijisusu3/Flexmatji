import drf from "@/api/drf"
import axios from "axios"

export default {
  state: {
    movies: [],
    movie: {},
    homeMovies:[],
    recommendMovies:[],
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    homeMovies: state => state.homeMovies,
    recommendMovies: state => state.recommendMovies
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_HOME_MOVIES:(state, homeMovies) => state.homeMovies = homeMovies,
    SET_MOVIE_COMMENTS:(state, comments) => (state.movie.movie_comments = comments),
    SET_RECOMMEND_MOVIES:(state, recommendMovies) => state.recommendMovies = recommendMovies
  },
  actions: {
    fetchRecommendMovies({commit, getters}){
      axios({
        url: drf.movies.movieRecommend(),
        method:'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_RECOMMEND_MOVIES', res.data)
          console.log(res.data)
        })
        .catch(err => console.error(err.response))
    },
    fetchHome({commit, getters}){
      axios({
        url:drf.movies.home(),
        method:'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_HOME_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchMovies({commit, getters}) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        // .catch(err => {
        //   console.error(err.response)
        //   if (err.response.status === 404) {
        //     router.push({ name: 'NotFound404' })
        //   }
        // })
    },
    likeMovie({commit, getters}, moviePk) {
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },
    createMovieComment({commit, getters}, {moviePk, content}){
      const comment = {content}
      axios({
        url:drf.movies.movieComments(moviePk),
        method:'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },
    updateMovieComment({ commit, getters }, { moviePk, movieCommentPk, content}){
      const comment = {content}
      axios({
        url: drf.movies.movieComment(moviePk, movieCommentPk),
        method:'put',
        data:comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },
    deleteMovieComment({commit, getters}, {moviePk, movieCommentPk}){
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.movieComment(moviePk, movieCommentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    }

  }
}