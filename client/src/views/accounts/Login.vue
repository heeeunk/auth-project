<template>
  <div class="login">
    <div class="login-container">
      <img src="@/assets/logo.png" alt="ssazip-login-img" />
      <p></p>
      <input type="text" name="userId" id="username" placeholder="ID" v-model="credentials.username">
      <input
        type="password"
        name="userPassword"
        id="userPassword"
        placeholder="PW"
        v-model="credentials.password"
      />
      <div>
        <button class="button-login" @click="login">로그인</button>
        <button class="button-cancel">취소</button>
      </div>
      <router-link to="/signup">
        <button class="button-signup" >회원가입하기</button>
      </router-link>
    </div>
    <img src="@/assets/background2.png" class="background-img-item"/>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      username: this.$store.username,
      token: this.$store.token,
      users:[],
    }
  },
  methods: {
    setToken: function (data) {
      const config = {
        Authorization: `JWT ${data}`
      }
      return config
    },
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          this.username = this.credentials.username
          this.$store.commit('getUserName', this.username);
          localStorage.setItem('jwt', res.data.token)
          this.$store.commit('getToken',res.data.token);
          this.$emit('login')
          
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/${this.username}/`,
            headers: this.setToken(res.data.token)
          })
            .then(res => {
              // 로그인한 유저가 관리자인 경우
              if (res.data.is_admin){
                this.$store.commit('getUsers',res.data.users);
                this.$router.push('/admin')
                // 일반 유저인 경우
              } else {
                this.$router.push('/home')
              }
            })
            .catch(err => {
              console.log(err)
            })
        })
        .catch(err => {
          console.log(err)
        })
    },
    getUsers: function(){
      console.log('ddddd')
      console.log('this.token')
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/userlist/',
        headers: this.setToken(this.token)
      })
        .then(
          this.$emit('login')
        )
        .catch(err => {
          console.log(err)
        })
    },
    goSignup: function(){
      this.$router.push('/signup')
    },
  }
}
  
</script>
<style scoped>
.login-container {
  background-color: rgb(240, 240, 248, 0.2);
  width: 500px;
  padding: 10px 0px;
  display: inline-block;
  border-radius: 30px;
  margin-top: 11vh;
} 

.login-container > input {
  width: 250px;
}

.login-container > img {
  width: 250px;
  margin-top: 30px;
}

.background-img {
  position: absolute;
  left: 0;
  height: 0;
  z-index: -1;
  height: 100%;
  width: 100%;
}

.login {
  display: inline-block;
  width: 100%;
  height: 100%;
}





.login > div > input, .login > div > input > img {
  display: block;
}

.login > div > input {
  border: none;
  margin: 20px auto;
  padding: 0 20px;
  height: 40px;

  background: #F0E9CC;
  border-radius: 20px;
  font-size: 25px;
  color: black;
}

.login > div > input:focus {
  outline: none;
}

.login .button-login, .login .button-cancel {
  border: none;
  border-radius: 20px;
  font-size: 20px;
  font-weight: 600;
  width: 125px;
  height: 40px;
  cursor: pointer;
  margin: 0 20px;
}
 .login .button-signup {
   border: none;
    border-radius: 20px;
    font-size: 20px;
    font-weight: 600;
    width: 300px;
    height: 40px;
    margin: 20px 0;
    margin-bottom: 40px;
 }

.button-login {
  background: #EAC16F;
}

.button-cancel {
  background: #CD5069;
  color: white;
  
}

.login > div > a > .button-signup {
  background: #9EACDD;
}

.background-img-item {
  position: absolute;
  bottom:0px;
  right:0px;
  width:100vw;
  height:40vh;
  z-index: -1;
}
</style>
