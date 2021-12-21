import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    users:[],
    token: '',
    username: '',
  },
  mutations: {
    getUsers: function(state, payload) {
        return state.users = payload
    },
    getToken: function(state, payload) {
        return state.token = payload
    },
    removeToken: function(state){
        return state.token = ''
    },
    getUserName: function(state, payload) {
        return state.username=payload
    }
  },
  actions: {
  },
  getters: {

    
  },
  modules: {
  }
})
