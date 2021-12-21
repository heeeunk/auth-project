<template>
  <div>
    <div class="text-container">
      <h1>
        <span>로</span>
        <span>그</span>
        <span>인</span>
        <span>완</span>
        <span>료</span>
        <span>!</span>
      </h1>
    </div>
    <div class="stage" >
      <img class="jump box bounce-7" src="@/assets/smilemates.png" alt="ssazip"/>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: function() {
    return {
      users: this.$store.state.users,
    }
  },

  methods: {
  
    
  },
  created: function () {

  },
  computed: {
  }
}
</script>

<style>
.reviews {
  position: absolute;
  top: 170px;
  left: 220px;
  width: 1100px
}
.review-table {
  margin-top:80px;
}
.go {
  text-align: center;
  margin-top: 35px;
}

.title{
  position:absolute;
  font-size:50px; 
  color:#FFFFFF; 
  bottom:60vh;
  left: 42vw;
}

.jump {
  width: 201px;
  height: 260px;
  position:absolute;
  bottom: 10vh;
  left: 45vw;
  animation: bounce .1s ease infinite alternate;
}

/* 뛰어다니는 모션 */
.stage {
    display: flex;
    height: 330px;
}

/* 캐릭터 크기 */
.box {
    align-self: flex-end;
    animation-duration: 2s;
    animation-iteration-count: infinite;
    height: 180px;
    margin: 0 auto 0 auto;
    transform-origin: bottom;
    width: 180px;
}
.bounce-7 {
    animation-name: bounce-7;
    animation-timing-function: cubic-bezier(0.280, 0.840, 0.420, 1);
}
@keyframes bounce-7 {
    0%   { transform: scale(1,1)      translateY(0); }
    10%  { transform: scale(1.1,.9)   translateY(0); }
    30%  { transform: scale(.9,1.1)   translateY(-100px); }
    50%  { transform: scale(1.05,.95) translateY(0); }
    57%  { transform: scale(1,1)      translateY(-7px); }
    64%  { transform: scale(1,1)      translateY(0); }
    100% { transform: scale(1,1)      translateY(0); }
}

.text-container {
  padding-top: 20vh;
  -webkit-font-smoothing: antialiased;
  display: flex;
  justify-content: center;
  align-items: center;
}

.text-container > h1 {
  height: 100px;
}

h1 span {
  position: relative;
  top: 20px;
  display: inline-block;
  animation: bounce .3s ease infinite alternate;
  font-size: 80px;
  color: #FFF;
  text-shadow: 0 1px 0 #CCC,
               0 2px 0 #CCC,
               0 3px 0 #CCC,
               0 4px 0 #CCC,
               0 5px 0 #CCC,
               0 6px 0 transparent,
               0 7px 0 transparent,
               0 8px 0 transparent,
               0 9px 0 transparent,
               0 10px 10px rgba(0, 0, 0, .4);
}
h1 span:nth-child(2) { animation-delay: .1s; }
h1 span:nth-child(3) { animation-delay: .2s; }
h1 span:nth-child(4) { animation-delay: .3s; }
h1 span:nth-child(5) { animation-delay: .4s; }
h1 span:nth-child(6) { animation-delay: .5s; }


@keyframes bounce {
  100% {
    top: -20px;
    text-shadow: 0 1px 0 #CCC,
                 0 2px 0 #CCC,
                 0 3px 0 #CCC,
                 0 4px 0 #CCC,
                 0 5px 0 #CCC,
                 0 6px 0 #CCC,
                 0 7px 0 #CCC,
                 0 8px 0 #CCC,
                 0 9px 0 #CCC,
                 0 50px 25px rgba(0, 0, 0, .2);
  }
}
</style>