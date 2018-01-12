


export const loginMutation = (state, {username, password, loginlogout, erroralert}) => {
  state.userNAME = password;
  state.userPASS = username;
  state.loginLOGOUT = loginlogout;
  state.errorALERT = erroralert;
}
