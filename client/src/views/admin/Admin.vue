<template>
  <div style="display:flex; justify-content:center; justify-align:center;">
    <table class="styled-table">
      <thead>
          <tr >
              <th style="text-align:center">아이디</th>
              <th>전화번호</th>
              <th>이메일</th>
              <th>관리자여부</th>
          </tr>
      </thead>
      <tbody>
         <tr v-for="(user, idx) in users" :key="idx" style="font-size: 20px;">
          <td>{{ user.username }}</td>
          <td>{{ user.phone }}</td>
          <td>{{ user.email }}</td>
          <td>
            <input type="checkbox" :id="'check'+idx" @click="checkBox(user)" v-model="user.is_admin" >
            <label ></label>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Admin',
  data: function() {
    return {
      users: this.$store.state.users,
      token: this.$store.token,
    }
  },
  methods: {
    checkBox(user){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/changeadmin/${user.username}/`,
      })
        .then(res => {  // eslint-disable-line no-unused-vars
          alert('관리자가 변경되었습니다.')
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/${this.username}/`,
            headers: this.setToken(this.token)
          })
            .then(res => {
              this.$store.commit('getUsers',res.data.users);
            })
            .catch(err => {
              console.log(err)
            })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
}
</script>

<style>
.styled-table {
  margin-top:30vh;
  border-collapse: collapse;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  text-align: center;
}

.styled-table thead tr {
    background-color: #e4cd4b;
    color: #523d10;
}

.styled-table th,
.styled-table td {
    padding: 12px 15px;
}

.styled-table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

.styled-table tbody tr:nth-of-type(odd) {
    background-color: #e9d6b4;
}

.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #e4cd4b;
}

.styled-table tbody tr.active-row {
    font-weight: bold;
    color: #e4cd4b;
}
</style>