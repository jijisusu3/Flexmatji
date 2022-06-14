<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
    <span class="imgtop">
      <img style="width:9rem; height:auto; padding:0; margin:0;" onclick="topFunction()" src="../src/assets/up.png" alt="">  
    </span>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
</style>
