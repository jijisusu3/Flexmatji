<template>
  <div>
    <section class="py-5 text-center container">
      <div class="col-lg-8 mx-auto">
        <img src="@/assets/커뮤니티.png" alt="">
        <nav class="nav d-flex justify-content-between">
          <router-link :to="{ name: 'community', params: { communityPk: 1 } }" class="p-2 link-secondary">
            공지사항
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 2 } }" class="p-2 link-secondary">
            자유게시판
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 3 } }" class="p-2 link-secondary">
            영화리뷰
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 4 } }" class="p-2 link-secondary">
            공포
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 5 } }" class="p-2 link-secondary">
            MARVEL
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 6 } }" class="p-2 link-secondary">
            애니메이션
          </router-link>
          <router-link :to="{ name: 'community', params: { communityPk: 7 } }" class="p-2 link-secondary">
            SF
          </router-link>
        </nav>
      </div>
    </section>

    <div v-for="article in articles" :key="article.pk">
      <ul class="list-group">
        <li class="list-group-item">
          <router-link 
            :to="{ name: 'article', params: { articlePk: article.id} }">
            {{ article.title }}
          </router-link>
        </li>
      </ul>
      <!-- 작성자 프로필로 이동 -->
      <!-- <router-link
        :to="{ name: 'profile', params: { username: article.user.username } }"
      >
        {{ article.user.username }} : 
      </router-link> -->
      
      <!-- 글 이동 링크 (제목) -->
      <!-- <router-link 
        :to="{ name: 'article', params: { articlePk: article.id} }">
        {{ article.title }}
      </router-link> -->

      <!-- 댓글 개수/좋아요 개수 -->
      <!-- =>
      댓글: ({{ article.comment_count }})  |  추천수: +{{ article.like_count }} -->

    </div>

    <div align="right" class="new-btn">
      <router-link class="nav-link" :to="{ name: 'articleNew' }">
        <button class="btn btn-secondary">글쓰기</button>
      </router-link>
    </div>

   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style scoped>
a {
  text-decoration-line: none;
  color: rgb(0, 0, 0);
}
li {
  margin: 0 10%;
}
.btn-group {
  align-items:center;
}
.new-btn {
  margin: 1rem 10% 1rem 1rem;
}
</style>
