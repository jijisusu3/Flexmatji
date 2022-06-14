<template>
  <nav class="navbar navbar-expand-xl bg-white my-3 mx-4">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name:'home' }">
        <img style="width:15rem; height:auto; padding:0; margin:3;" src="@/assets/reallast.png" alt="">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent" >
        <ul class="navbar-nav me-auto mb-1 width-auto">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'movies' }">
              <font class="bold mx-0 py-3" size="6px">
                <b>Today's Movie</b>
              </font>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'articles' }">
              <font size="6px mx-5 py-3">
                <b>Community</b>
              </font>
            </router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <font size="6px mx-5 py-3">
                <b>My</b>
              </font>
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li>
                <router-link class="dropdown-item" :to="{ name: 'myMovie', params: { username: currentUser.username} }">
                  <font size="4px">
                    내 영화 목록
                  </font>
                </router-link>
              </li>
              <li><hr class="dropdown-divider"></li>
              <li>
                <a class="dropdown-item" :href="`http://localhost:8080/profile/${username}`">
                  <font size="4px">
                    내 프로필
                  </font>
                </a>          
              </li>
            </ul>
          </li>
        </ul>
        <div class="px-2">
          <button class="btn btn btn-outline-secondary my-2" v-if="isLoggedIn">
            <router-link class="nav-link" :to="{ name: 'logout' }">
              <font size="4px">
                Logout
              </font>
            </router-link>
          </button>
        </div>

        <!-- <form @submit.prevent="onSubmit" class="movie-comment-list-form">
          <input type="text" v-model="content" required class="form-control">
          <button>Comment</button>
        </form> -->
        <form class="d-flex" role="search">
          <input type="text" v-model="content" class="form-control me-2" placeholder="Search" aria-label="Search">
          <router-link
            :to="{ name: 'movie', params: {moviePk: content} }"
          >
            <button class="btn btn-outline-success" type="submit">Search</button>
          </router-link>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {

    name: 'NavBar',
    data(){
      return {
        content:''
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods:{
      searchMovie(){
        this.router.navigate([`/movies/12`])
        this.content=''
      }
    }
  }
</script>
<style scoped>
.nav {
  list-style-type: none;
  text-align: center;
  margin: 0;
  padding: 0;
}
.nav li {

  display: inline-block;
  padding: 20px;
}

</style>
