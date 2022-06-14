<template>
  <div class="container">
    <form @submit.prevent="onSubmit" class="movie-comment-list-form row">
      <input type="text" class="form-control" aria-describedby="inputGroup-sizing-lg"  v-model="content" required placeholder="댓글을 입력하세요." aria-label="Recipient's username">
      <button class="btn btn-secondary" id="button-addon2">댓글 등록</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MovieCommentListForm',
  data() {
    return {
      content: '',
    }
  },
  computed:{
    ...mapGetters(['movie'])
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ moviePk: this.movie.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style scoped>
.movie-comment-list-form {
  margin: 1rem;
  padding: 1rem;
}
</style>