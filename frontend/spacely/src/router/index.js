import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Spacely from '@/components/Spacely'
import Splash from '@/components/Splash'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Splash',
      component: Splash
    },
    {
      path: '/spacely',
      name: 'Spacely',
      component: Spacely
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
