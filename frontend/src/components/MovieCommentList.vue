<template>
  <div class="movie-comment-list">
    <div>
      <movie-comment-list-item
        v-for="movieComment in movieComments"
        :movieComment="movieComment"
        :key="movieComment.pk"
      >
      </movie-comment-list-item>
    </div>
    <movie-comment-list-form></movie-comment-list-form>
  </div>
</template>

<script>
import MovieCommentListForm from '@/components/MovieCommentListForm.vue'
import MovieCommentListItem from '@/components/MovieCommentListItem.vue'

export default {
  name:'MovieCommentList',
  components:{
    MovieCommentListForm,
    MovieCommentListItem
  },
  props:{
    movieComments: Array,
  }
}
</script>

<style>
</style>