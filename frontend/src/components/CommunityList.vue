<template>
  <div>
    <div v-for="article in community.article_find" :key="article.pk">
      <ul class="list-group">
        <li class="list-group-item">
          <router-link 
            :to="{ name: 'article', params: { articlePk: article.id} }">
            {{ article.title }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'CommunityList',
  computed: {
    ...mapGetters(['community'])
  },
  methods: {
    ...mapActions(['fetchCommunity'])
  },
  created() {
    this.fetchCommunity(this.communityPk)
  }
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
</style>