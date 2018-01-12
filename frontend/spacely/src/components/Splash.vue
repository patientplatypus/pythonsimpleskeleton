<template>
  <div class="splash">
    <h1>
      This is splash page
    </h1>
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
