<template>
  <div class="login">
    <div class="login-container">
      <img src="@/assets/logo.png" alt="logo-img" />
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
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials,
      })
        .then(res => {
          const data=JSON.parse(res.data)
          const username = data.user.username
          const token = data.token
          this.username = username
          this.$store.commit('getUserName', username);
          this.$store.commit('getToken', token);
          localStorage.setItem('jwt', token)
          this.$emit('login')
          
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/${this.username}/`,
            headers: this.setToken(token)
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
/* 로그인 투명 컨테이너 내부 */
.login-container {
  background-color: rgb(240, 240, 248, 0.2);
  width: 500px;
  padding: 10px 0px;
  display: inline-block;
  border-radius: 30px;
  margin-top: 17vh;
} 
.login-container > input {
  width: 250px;
  outline-color: #ebb34b;
  display: block;
  border: none;
  margin: 20px auto;
  padding: 0 20px;
  height: 40px;
  background: #F0E9CC;
  border-radius: 20px;
  font-size: 25px;
  color: black;
}
.login-container > img {
  width: 250px;
  margin-top: 30px;
}

/* 버튼 */
.button-login, .button-cancel {
  border: none;
  border-radius: 20px;
  font-size: 20px;
  font-weight: 600;
  width: 125px;
  height: 40px;
  cursor: pointer;
  margin: 0 20px;
  box-shadow: 1px 4px 0 rgb(0,0,0,0.5)
}
.button-login:active { 
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5); 
  position: relative; 
  top:2px; 
}
.button-cancel:active { 
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5); 
  position: relative; 
  top:2px; 
}
 .button-signup {
   border: none;
    border-radius: 20px;
    font-size: 20px;
    font-weight: 600;
    width: 300px;
    height: 40px;
    margin: 20px 0;
    margin-bottom: 40px;
    cursor: pointer;
    background: #9EACDD;
    box-shadow: 1px 4px 0 rgb(0,0,0,0.5)
 }
 .button-signup:active { 
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5); 
  position: relative; 
  top:2px; 
 }
.button-login {
  background: #EAC16F;
}
.button-cancel {
  background: #CD5069;
  color: white;
  
}

/* 배경에 캐릭터 이미지 */
.background-img-item {
  position: absolute;
  bottom:0px;
  right:0px;
  width:100vw;
  height:40vh;
  z-index: -1;
}
</style>
