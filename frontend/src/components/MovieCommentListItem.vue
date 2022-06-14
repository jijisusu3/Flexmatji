<template>
  <ul class="movie-comment-list-item">
    <router-link :to="{ name: 'profile', params: { username: movieComment.user.username } }">
      {{ movieComment.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate" class="btn btn-outline-secondary">Update</button>
       |
      <button @click="switchIsEditing" class="btn btn-outline-secondary">Cancle</button>
    </span>

    <span v-if="currentUser.username === movieComment.user.username && !isEditing">
      <button @click="switchIsEditing" class="btn btn-outline-secondary">Edit</button>
       |
      <button @click="deleteMovieComment(payload)" class="btn btn-outline-secondary">Delete</button>
    </span>
  </ul>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MovieListItem',
  props:{ movieComment: Object},
  data(){
    return {
      isEditing:false,
      payload:{
        moviePk: this.movieComment.movie,
        movieCommentPk:this.movieComment.pk,
        content: this.movieComment.content
      }
    }
  },
  computed:{
    ...mapGetters(['currentUser']),
  },
  methods:{
    ...mapActions(['updateMovieComment', 'deleteMovieComment']),
    switchIsEditing(){
      this.isEditing = !this.isEditing
    },
    onUpdate(){
      this.updateMovieComment(this.payload)
      this.isEditing=false
    }
  }
}
</script>

<style scoped>
a {
  text-decoration-line: none;
  color: #e130d8;
}
.movie-comment-list-item {
  margin: 0.1rem;
}
</style>