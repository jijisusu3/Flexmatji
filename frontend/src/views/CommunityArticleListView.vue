<template>
  <div>
    <section class="py-5 text-center container">
      <h3>{{community.name}}</h3>
    </section>
    <community-list></community-list>
    <div align="right" class="new-btn">
      <router-link class="nav-link" :to="{ name: 'articleNew' }">
        <button class="btn btn-secondary">글쓰기</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'CommunityArticleList',
  components: { CommunityList },
  data() {
    return {
      communityPk: this.$route.params.communityPk
    }
  },
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
.new-btn {
  margin: 1rem 10% 1rem 1rem;
}
</style>