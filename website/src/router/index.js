import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/myPage',
    name: 'myPage',
    component: () => import('../views/myPage.vue')
  },
  {
    path: '/testForm',
    name: 'testForm',
    component: () => import('../views/testForm.vue')
  },
  // {
  //   path: '/backendEng',
  //   name: 'backendEng',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/backendEng.vue')
  // },
  // {
  //   path: '/frontendEng',
  //   name: 'frontendEng',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/frontendEng.vue')
  // },
  // {
  //   path: '/searchBox',
  //   name: 'searchBox',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/searchBox.vue')
  // }
]

const router = new VueRouter({
  routes
})

export default router
