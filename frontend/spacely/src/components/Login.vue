<template>
  <div class="login">
    <h1>
      hello this is login page
    </h1>
    <input v-model="usernameInput" placeholder="enter username"/>
    <input v-model="passwordInput" placeholder="enter password"/>
    <button v-on:click='loginButton()'>Login</button>
    <button v-on:click='signupButton()'>Sign Up</button>
    <button v-on:click='showdbButton()'>Show DB</button>
    <div>
      <h2>
        The value of login/logout is: {{loginLOGOUT}}
      </h2>
    </div>
    <div>
      <h2>
        The value of error alert is: {{errorALERT}}
      </h2>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import EventBus from '../bus/EventBus';
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      usernameInput: '',
      passwordInput: ''
    }
  },
  computed: {
   ...mapGetters([
     'userNAME',
     'userPASS',
     'loginLOGOUT',
     'errorALERT',
   ])
  },
  methods:{
    ...mapActions([
     'loginAction',
     'signupAction',
     'showdbAction',
     'reseterrorAction'
    ]),
    loginButton: function(){
      if (this.usernameInput!=''&&this.passwordInput!=''){
        this.loginAction({username: this.usernameInput, password: this.passwordInput})
      }else{
        alert('Neither username nor password can be blank!')
      }
    },
    signupButton: function(){
      if (this.usernameInput!=''&&this.passwordInput!=''){
        this.signupAction({username: this.usernameInput, password: this.passwordInput})
      }else{
        alert('Neither username nor password can be blank!')
      }
    },
    showdbButton: function(){
      this.showdbAction()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
