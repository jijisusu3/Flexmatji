<template>
  <div>
    <section class="py-5 container">
      <div class="article-box">
        <h3 class="text-center">{{ article.title }}</h3>
        <p>
          작성자: 
          <router-link :to="{ name: 'profile', params: { username: article.user.username } }">
            {{ article.user.username }}
          </router-link>
        </p>
        <p>
          {{ article.content }}
        </p>
      </div>
    <hr>

    <div align="right" class="btn-box">
      <!-- Article Edit/Delete UI -->
      <div v-if="isAuthor" class="ud">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button class="btn btn-outline-secondary">Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articlePk)" class="btn btn-outline-secondary">Delete</button>
      </div>

      <!-- Article Like UI -->
      <div class="like">
        Likeit:
        <button class="btn btn-secondary"
          @click="likeArticle(articlePk)"
        >{{ likeCount }}</button>
      </div>
    </div>

    <hr>
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

    <!-- 목록으로 이동 -->
      <div align="right" class="back">
        <router-link :to="{ name: 'articles' }"  class="ud-btn">
          목록
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      console.log(this.articlePk)
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style scoped>
a {
  text-decoration-line: none;
  color: #e130d8;
}
h3 {
  padding: 1rem;
}
.article-box {
  padding: 1rem;
  margin: 1rem;
}
.btn-box {
  display: flex;
  flex-direction: column;
}
.ud {
  margin: 0.3rem 10% 0.3rem 0.3rem;
}
.ud-btn {
  text-decoration-line: none;
  color: black;
}
.like {
  margin: 0.3rem 10% 0.3rem 0.3rem;
}
.back {
  margin: 1rem;
}
</style>
