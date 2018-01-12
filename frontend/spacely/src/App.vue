<template>
  <div id="app">
    <br/><br/>
    <div class='topbox'>
      <router-link class='routerlink' to="/">Splash</router-link>
      <router-link class='routerlink' to="/spacely">Spacely</router-link>
      <router-link class='routerlink' to="/login">Login</router-link>
    </div>
    <div class='contentbox'>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 15vw 85vw;
  grid-template-rows: 10vh 90vh;
  grid-gap: 0vw;
  overflow: hidden;
}

.contentbox{
  grid-column: 1 / 3;
  grid-row: 2 / 3;
  background-color: grey;
  overflow: hidden;
  overflow-y: scroll;
}

.topbox{
  grid-column: 1 / 3;
  grid-row: 1 / 2;
  background-color: skyblue;
  padding-top: 0.75%;
}
</style>
