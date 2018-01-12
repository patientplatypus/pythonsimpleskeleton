import axios from 'axios'

import store from './index'



export const loginAction = ({ commit }, {username, password}) => {

  axios.post('http://127.0.0.1:5000/login_logout',{
    username: username,
    password: password,
    loginlogout: false
  })
  .then(response=>{
    console.log("response from loginAction: ", response);
    if (response.data==="didnotfinduser" || response.data==="didnotverifypassword"){
      let erroralert = response.data;
      let loginlogout = false;
      commit('loginMutation',{username, password, loginlogout, erroralert})
    }else if (response.data==="True" || response.data==="False"){
      let erroralert = 'statusnormal'
      let loginlogout = response.data==="True"?true:false
      commit('loginMutation',{username, password, loginlogout, erroralert})
    }
  })
  .catch(error=>{
    console.log("PANIC ERROR IN loginAction : ", error);
  });
}

export const signupAction = ({ commit }, {username, password}) => {

  axios.post('http://127.0.0.1:5000/add_user', {
    username: username,
    password: password
  })
  .then(response=>{
    console.log("response from signupAction: ", response);
    if (response.data === "True"){
      console.log('inside response.data===true in signupAction');
      let erroralert = 'statusnormal'
      let loginlogout = true;
      commit('loginMutation',{username, password, loginlogout, erroralert})
    }else{
      let erroralert = 'useralreadyexists'
      let loginlogout = false;
      commit('loginMutation',{username, password, loginlogout, erroralert})
    }
  })
  .catch(error=>{
    console.log("PANIC ERROR IN signupAction: ", error);
  });

}

export const showdbAction = ({ commit }) => {

  axios.get('http://127.0.0.1:5000/show_db')
  .then(response=>{
    console.log("response from showdbAction: ", response);
  })
  .catch(error=>{
    console.log("PANIC ERROR IN showdbAction: ", error);
  });

}

export const reseterrorAction = ({ commit }) => {

}
