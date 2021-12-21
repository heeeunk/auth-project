<template>
  <div id="app">
    <div id="nav" class="nav">
      <div v-if="isLogin">
        <div class="greeting" style="display:inline-block;">
          {{$store.state.username}}님 안녕하세요
          <router-link @click.native="logout" to="#" class="logout">Logout</router-link>
        </div>
      </div>
      <div v-else>
        <div class="greeting" style="display:inline-block;">
          로그인을 해주세요.
        </div>
      </div>
    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: function () {
    return {
      isLogin: false
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$store.commit('removeToken');
      this.$router.push({ name: 'Login' })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  background: url(./assets/background.jpg);
}

.nav{
  position:fixed;
  right:0px;
}

#nav a {
  font-weight: bold;
  color: #EAC16F;
}

.logout {
  color: #42b983;
  text-decoration-line: none;
  margin-left:20px;
}

.greeting {
  /* float:right; */

  width: 380px;
  height: 45px;
  background-color: rgba(248, 250, 252, 0.267);
  color:white; 
  font-size:25px;
  line-height:50px;
  border-radius: 1rem;
  margin-top:20px;
  margin-right:20px;
}
</style>
