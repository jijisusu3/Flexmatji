<template>
  <div>
    <section class="text-center container pt-5">
      <img style="height:15rem; width:auto; padding-top:15px;" src="@/assets/Signup.png" alt="">
    </section>
    <account-error-list v-if="authError"></account-error-list>

    <div class="login-page">
      <div class="form">
        <form @submit.prevent="signup(credentials)" class="register-form">
          <input v-model="credentials.username" type="text" placeholder="username" required/>
          <input v-model="credentials.password1" type="password" placeholder="password" required/>
          <input v-model="credentials.password2" type="password" placeholder="password를 한번 더 입력해주세요." required/>
          <button>create</button>
          <p class="message">Already registered?
            <router-link :to="{ name: 'login' }">
              Log In
            </router-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style scoped>
.login-page {
  width: 360px;
  padding: 0% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #e130d8;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #c58db9;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4c54af;
  text-decoration: none;
}
/* .form .register-form {
  display: none;
} */
</style>
