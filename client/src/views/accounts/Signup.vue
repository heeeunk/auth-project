<template>
  <div>
    <div class="">
    <img src="@/assets/background2.png" class="background-img-item"/>
      <div class="join-container">
        <p class="account-title">회원가입</p>
        <!-- 아이디 -->
        <div>
          <div>
            <label for="name" class="input-label name-label">아이디</label>
            <input
              type="text"
              id="name"
              placeholder="20자 이내로 입력해주세요."
              onfocus="this.placeholder=''"
              onblur="this.placeholder='20자 이내로 입력해주세요.'"
              v-model="credentials.username"
            />
          </div>
          <h6 v-if="error.username == 'notValid'" class="name-warning" style="color:red">
            아이디 길이는 1자 이상, 20자 이하입니다.
          </h6>
        </div>
        <!-- 비밀번호 -->
        <div>
          <label for="password" class="input-label" style="margin-left:-25px">비밀번호</label>
          <input
            type="password"
            id="password"
            placeholder="영문, 숫자 포함 8자 이상 16자 이하로 입력해주세요."
            onfocus="this.placeholder=''"
            onblur="this.placeholder='영문, 숫자 포함 8자 이상 16자 이하로 입력해주세요.'"
            v-model="credentials.password"
          />
        </div>
        <h6 v-if="error.password == 'notValid'" class="account-warning" style="color:red">
          비밀번호 양식이 맞지 않습니다.
        </h6>
        <!-- 비밀번호 재입력 -->
        <div>
          <label for="password-confirm" class="input-label" style="margin-left:-85px">비밀번호 확인</label>
          <input
            type="password"
            id="password-confirm"
    
            placeholder="비밀번호 확인을 입력해주세요."
            v-model="credentials.passwordConfirmation"
          />
        </div>
        <br />
        <h6 v-if="error.passwordConfirmation == 'notSame'" class="password-confirm-warning" style="color:red">
          비밀번호가 일치하지 않습니다!
        </h6>

        <!-- 전화번호 입력 -->
        <div>
          <div>
            <label for="phone" class="input-label" style="margin-left:-25px">전화번호</label>
            <input
              type="text"
              id="phone"
              placeholder="ex) 01012345678"
              onfocus="this.placeholder=''"
              onblur="this.placeholder='ex) 01012345678'"
              v-model="credentials.phone"
            />
          </div>
          <h6 v-if="error.phone == 'notValid'" class="phone-number-warning" style="color:red">
            전화번호 양식이 맞지 않습니다.
          </h6>
        </div>
        <!-- 이메일 입력 -->
        <div class="d-flex email-container">
          <label for="email" class="input-label" style="margin-left:-175px">이메일</label>
          <input
            type="text"
            id="email"
            placeholder="40자 이내로 입력해주세요."
            onfocus="this.placeholder=''"
            onblur="this.placeholder='40자 이내로 입력해주세요.'"
            v-model="credentials.email"
          />
          <!-- 중복체크 버튼 -->
          <!-- <div class="check-button" @click="emailcheck(credentials.email)">
            <ButtonSquare text="중복체크" />
          </div> -->
          <br />
          <br />
        </div>
        <h6 v-if="error.email == 'styleError'" class="email-warning" style="color:red">
          이메일 형식이 일치하지 않습니다.
        </h6>
        <h6 v-if="error.email == 'lengthError'" class="email-warning" style="color:red">
          이메일은 최대 30자 이상이어야 합니다.
        </h6>

        <div class="d-flex justify-content-center button-container">
          <!-- 돌아가기 버튼 -->
          <!-- <div class="back-button">
            <router-link to="/"><ButtonRound text="돌아가기"/></router-link>
          </div> -->
          <!-- 가입 버튼 -->
          <div>
            <button class="join-button" @click="signup(credentials)">회원가입</button>
            <!-- <ButtonRound text="가입하기" /> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import * as EmailValidator from 'email-validator';
import PV from 'password-validator';

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        phone: '',
        email: '',
      },
      error: {
        username: '',
        password: '',
        passwordConfirmation: '',
        phone: '',
        email: '',
      },
      passwordSchema: new PV(),
    }
  },
  methods: {
    signup: function () {
      // 비밀번호입력값와 비밀번호확인값이 같은 경우에만 통신요청
      if (this.credentials.password == this.credentials.passwordConfirmation){
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
          data: this.credentials,
        })
          .then(res => { // eslint-disable-line no-unused-vars
            alert('회원가입 성공!')
            this.$router.push({ name: 'Login' })
          })
          .catch(err => {
            console.log(err)
            console.log(err)

          })
      }else{
        alert('입력하신 비밀번호와 비밀번호 확인값이 다릅니다.')
      }
    },
    checkform() {
      console.log(this.credentials)
      this.isSubmit = false;
      // 이름의 길이가 1자 이상, 20자 이하인가?
      if (this.credentials.username.length <= 0 || this.credentials.username.length > 20) {
        this.error.username = 'notValid';
        return;
      } else this.error.username = true;

       // 비밀번호가 적합한가?
      if (!this.passwordSchema.validate(this.credentials.password)) {
        this.error.password = 'notValid';
        return;
      } else this.error.password = true;

      // 비밀번호 확인
      if (this.credentials.passwordConfirmation.length > 0 && this.credentials.password != this.credentials.passwordConfirmation) {
        this.error.passwordConfirmation = 'notSame';
        return;
      } else this.error.passwordConfirmation = true;

      // 이메일 형식이 맞는가?
      if (!EmailValidator.validate(this.credentials.email)) {
        this.error.email = 'styleError';
        return;
      }

      // 이메일 길이가 1글자 이상, 40글자 미만인가?
      else if (this.credentials.email.length <= 0 || this.credentials.email.length >= 40) {
        this.error.email = 'lengthError';
        return;
      } else this.error.email = true;

      // 전화번호
      if (this.credentials.phone.length != 11 || this.credentials.phone.slice(0, 3) != '010') {
        this.error.phone = 'notValid';
        return;
      } else this.error.phone = true;

      this.isSubmit = true;
    },
  },
  // 입력 변수 감시
  watch: {
    'credentials.username': function() {
      this.checkform();
    },
    'credentials.phone': function() {
      this.checkform();
    },
    'credentials.email': function() {
      this.checkform();
    },
    'credentials.password': function() {
      this.checkform();
    },
    'credentials.passwordConfirmation': function() {
      this.checkform();
    },
  },
  created() {
  // 패스워드 규칙. 최소 8자 ~ 최대 100자. 숫자와 문자 포함해야함.
  this.passwordSchema
    .is()
    .min(8)
    .is()
    .max(16)
    .has()
    .digits()
    .has()
    .letters();
  },
}
</script>

<style scoped>
/* 반투명 배경 */
.join-container {
  background-color: rgb(253, 251, 251, 0.2);
  width: 700px;
  height: 500px;
  margin-top: 100px;
  border-radius: 2rem;
  padding-top: 20px;
  display: inline-block;
}

/* 큰 제목 */
p {
  font-size: 30px;
  font-weight: bold;
  font-family: 'Noto Sans KR', sans-serif;
  color: #f59c35;
  text-align: left;
  margin-left: 100px;
  /* margin-top: 35px; */
  margin-bottom: 25px;
}

.join-container label {
  font-size: 20px;
  font-weight: bold;
}

/* 전체 input 태그 CSS */
input {
  padding-left: 15px;
  border-style: none;
}

input:focus {
  outline: none;
}

/* 전체 input-label CSS */
.input-label {
  font-family: 'Godo';
  color: #f9d479;
  /* font-size: 25px; */
  margin-right: 15px;
}

/* 계정 등록 전체 영역 */
.account-input {
  width: 400px;
  height: 40px;
  border-radius: 0.5rem;
  margin-bottom: 40px;
}

/* 이메일 입력 전체 영역 */
.email-container {
  margin-left: 173px;
}

/* 이메일 입력칸 */
.email-input {
  margin-right: 20px;
}


/* 비밀번호 확인 입력칸 */
.password-confirm-input {
  margin-right: 240px;
}

/* 정보 등록 전체 영역 */
.info-input {
  width: 250px;
  height: 40px;
  border-radius: 0.5rem;
  margin-bottom: 40px;
}

.join-container input{
  border: none;
  margin: 15px auto;
  padding: 0 20px;
  height: 30px;
  width:250px;
  background: #f7f6f4;
  border-radius: 0.5rem;
  font-size: 15px;
  color: black;
}

/* 전화번호 입력칸 */
.phone-input {
  margin-right: 60px;
}

/* 기수 입력칸 */
.grade-input {
  margin-right: 60px;
}

/* 참여코드 입력칸 */
.code-input {
  margin-right: 20px;
}

/* 마지막 열 입력칸 전체 부분 */
.last-row-input {
  margin-left: 17px;
}

/* 중복체크 버튼 */
.check-button .btn-light {
  font-family: 'Godo';
  font-size: 18px;
  height: 40px;
  color: white;
  background-color: #1c84c4;
  border-style: none;
  border-radius: 0.5rem;
}

/* 돌아가기 버튼 */
.back-button .btn-light {
  font-family: 'Godo';
  font-size: 23px;
  width: 170px;
  height: 60px;
  margin-top: 10px;
  margin-right: 50px;
  color: #1f4256;
  background-color: #e1af4e;
  border-style: none;
}

/* 회원가입 버튼 */
.join-button {
  background-color: #99b7ff;
  border: none;
  border-radius: 20px;
  font-size: 20px;
  font-weight: 600;
  width: 125px;
  height: 40px;
  cursor: pointer;
  margin: 0 20px;
}

/* SSAZIP 여러 개 모인 이미지 */
.eggs {
  position: absolute;
  width: 370px;
  height: 200px;
  top: 310px;
  right: 470px;
}

/* 계정 경고 메시지 */
.account-warning {
  position: absolute;
  margin-top: -10px;
  margin-left: 270px;
}

/* 계정 경고 메시지 */
.password-confirm-warning {
  position: absolute;
  margin-top: -20px;
  margin-left: 270px;
}

/* 이름 경고 메시지 */
.name-warning {
  position: absolute;
  margin-top: -10px;
  margin-left: 250px;
}

/* 전화번호 경고 메시지 */
.phone-number-warning {
  position: absolute;
  margin-top: -30px;
  margin-left: 105px;
}

/* 기수 경고 메시지 */
.email-warning {
  position: absolute;
  margin-top: -30px;
  margin-left: 250px;
}

.account-title {
  margin-top: 15px;
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