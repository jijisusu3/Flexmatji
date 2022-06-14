<template>
  <div>
    <div class="contact-area">
      <div class="contact">
        <section>
          <div class="content">
            <div class="card">
              <!-- <img src="../assets/logo.png" class="card-img-top" alt=""> -->
              <div class="card-body mycard">
                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-emoji-sunglasses" viewBox="0 0 16 16">
                  <path d="M4.968 9.75a.5.5 0 1 0-.866.5A4.498 4.498 0 0 0 8 12.5a4.5 4.5 0 0 0 3.898-2.25.5.5 0 1 0-.866-.5A3.498 3.498 0 0 1 8 11.5a3.498 3.498 0 0 1-3.032-1.75zM7 5.116V5a1 1 0 0 0-1-1H3.28a1 1 0 0 0-.97 1.243l.311 1.242A2 2 0 0 0 4.561 8H5a2 2 0 0 0 1.994-1.839A2.99 2.99 0 0 1 8 6c.393 0 .74.064 1.006.161A2 2 0 0 0 11 8h.438a2 2 0 0 0 1.94-1.515l.311-1.242A1 1 0 0 0 12.72 4H10a1 1 0 0 0-1 1v.116A4.22 4.22 0 0 0 8 5c-.35 0-.69.04-1 .116z"/>
                  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-1 0A7 7 0 1 0 1 8a7 7 0 0 0 14 0z"/>
                </svg>
                <h5 class="card-title my-3"><h1>{{ profile.username }}'s Profile</h1></h5>
                <p v-if="currentUser.username !== profile.username">
                  <button class="btn btn-outline-secondary my-3" @click="followUser(profile.id)">
                  <i class="fa-solid fa-heart" style="color:crimson;"></i>
                  </button>
                </p>

                <h5 type="button" class="btn btn-secondary btn-sm" data-bs-toggle="modal" data-bs-target="#exampleModal">
                  팔로워
                </h5>
                : {{followerCount}}  /  
                <div focus="false" class="modal fade" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="flase">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">{{ profile.username }}를 팔로우한 목록</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <div data-bs-dismiss="modal" v-for="follower in profile.followers" :key="follower.id" class="mybox1">
                          <ul class="list-group">
                            <li class="list-group-item">
                              <a :href="`http://localhost:8080/profile/${follower.username}`">
                                {{ follower.username }}
                              </a>
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>



                <h5 type="button" class="btn btn-secondary btn-sm" data-bs-toggle="modal" data-bs-target="#exampleModal1">
                  팔로잉
                </h5>
                : {{followingCount}}
                <div focus="false" class="modal fade" id="exampleModal1" aria-labelledby="exampleModalLabel1" aria-hidden="flase">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel1">{{ profile.username }}가 팔로잉한 목록</h5>
                        <button type="button2" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <div data-bs-dismiss="modal" v-for="following in profile.followings" :key="following.id" class="mybox1">
                          <ul class="list-group">
                            <li class="list-group-item">
                              <a :href="`http://localhost:8080/profile/${following.username}`">
                                {{ following.username }}
                              </a>
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button type="button2" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </section>
      </div>
      <div class="articlebox">
        <div v-if="currentUser.username === profile.username" class="mybox">
          <h3 class="text-center">내가 작성한 글</h3>
          <div v-for="article in profile.articles" :key="article.pk" class="mybox1">
            <ul class="list-group">
              <li class="list-group-item">
                <router-link 
                  :to="{ name: 'article', params: { articlePk: article.pk} }">
                  {{ article.title }}
                </router-link>
              </li>
            </ul>
          </div>
          <h3 class="text-center">좋아요 한 글</h3>
            <div v-for="article in profile.like_articles" :key="article.pk">
              <ul class="list-group">
                <li class="list-group-item">
                  <router-link 
                    :to="{ name: 'article', params: { articlePk: article.pk} }">
                    {{ article.title }}
                  </router-link>
                </li>
              </ul>
            </div>
        </div>
      </div>
    </div>
    <div class="py-5 bg-light">
      <h3 class="text-center"><b>{{profile.username}}님이 찜한 영화</b></h3>
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
            <div v-for="movie in profile.like_movie" :key="movie.id">
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
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  data() {
    return {
      userPk: this.$route.params.userPk,
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    followerCount() {
      return this.profile.followers?.length
    },
    followingCount() {
      return this.profile.followings?.length
    },

  },
  methods: {
    ...mapActions(['fetchProfile', 'followUser']),

  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    
  },
}
</script>

<style scoped>
  a {
    text-decoration-line: none;
    color: rgb(0, 0, 0);
  }
  .contact-area {
    width: 100%;
    height: auto;
    position: relative;
  }

  .contact {
    position: relative;
    max-width: 420px;
    padding: 40px 20px;
    overflow: hidden;
    margin: 0 auto;
  }    
  section {
    border-radius: 5px;
    float: left;
    width: 100%;
  }     
  .content {
    float: left;
    width: 100%;
    padding: 20px 30px 20px 30px;
    position: relative;
    text-align: center;
  }
  .bi-emoji-sunglasses{
    font-size: 50px;
  }
  svg{
    color: #e130d8;
    width: 100px;
    height: 100px;
  }
.mybox {
  margin: 1rem 20% 1rem 20%;
}
h3 {
  margin: 1rem;
}
.mycard {
  margin: 1rem;
}
.articlebox {
  margin-bottom: 3rem;
}

</style>