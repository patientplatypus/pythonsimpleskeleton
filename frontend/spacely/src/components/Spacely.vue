<template>
  <div class="spacely">
    <br/><br/>
    <div>
      <h1>
        Hello, this is spacely page
      </h1>
    </div>
    <div class="menubox">
      <div class='menuboxflex'>
        <div v-bind:style='{flex: "1", width:"100%"}'></div>
        <div v-bind:style='{flex: "1", width:"100%"}'>
          <p>
            Menu Item 1
          </p>
        </div>
        <div v-bind:style='{flex: "1", width:"100%"}'>
          <p>
            Menu Item 2
          </p>
        </div>
        <div v-bind:style='{flex: "1", width:"100%"}'>
          <p>
            Menu Item 3
          </p>
        </div>
        <div v-bind:style='{flex: "1", width:"100%"}'>
          <p>
            Menu Item 4
          </p>
        </div>
        <div v-bind:style='{flex: "1", width:"100%"}'>
          <p>
            Menu Item 5
          </p>
        </div>
        <div v-bind:style='{flex: "1", width:"100%"}'></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import EventBus from '../bus/EventBus';
export default {
  name: 'Spacely',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  // computed: {
  //  ...mapGetters([
  //    'userName',
  //    'userPass',
  //    'userPic',
  //    'userObj',
  //    'userVotes',
  //    'socket',
  //    'channel',
  //    'connectStatus',
  //    'messages',
  //    'returnmessage',
  //    'articlesList',
  //    'commentsList',
  //  ])
  // },
  methods:{
    // ...mapActions([
    //  'socketConnect',
    //  'channelPushArticle',
    //  'getArticles',
    //  'articleVote',
    //  'commentVote',
    //  'sendComment',
    //  'handleCommentChannel',
    //  'getArticleComments',
    //  'getUserObj'
    // ]),
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spacely{
  background-color: rgba(100,100,100,1);
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 5vw 20vw 10vw 65vw;
  grid-template-rows: 40vh 30vh 10vh 10vh;
  grid-gap: 0vw;
}
.menubox{
  grid-column: 2/3;
  grid-row: 2/4;
  background-color: orange;
}
.menuboxflex{
  display: flex;
  flex-direction: column;
  background-color: rgba(50,50,50,1);
  color: rgba(200,200,200,0.8);
  text-align: center;
  height: 100%;
  font-size: 2vh;
}

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
