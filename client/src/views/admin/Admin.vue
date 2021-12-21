<template>
  <div style="display:flex; justify-content:center; justify-align:center;">
    <table class="styled-table">
      <thead>
          <tr>
              <th>아이디</th>
              <th>전화번호</th>
              <th>이메일</th>
              <th>관리자여부</th>
          </tr>
      </thead>
      <tbody>
         <tr v-for="(user, idx) in users" :key="idx" @click="selectReview(review)"  style="font-family: 'Jua', sans-serif; font-size: 20px;">
          <td>{{ user.username }}</td>
          <td>{{ user.phone }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.is_admin }}</td>
        </tr>

      </tbody>
    </table>
  </div>
</template>

<script>
// import { mapGetters, mapState } from 'vuex'
// import axios from 'axios'

export default {
  name: 'Admin',
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
    // ...mapState([
    //   'reviews',
    // ]),
    // ...mapGetters([
    //   'setToken',
    // ])
  }
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
}

.styled-table thead tr {
    background-color: #e4cd4b;
    color: #523d10;
    text-align: left;
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