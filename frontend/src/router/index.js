
import { createWebHistory, createRouter } from "vue-router";
import FundamentalList from '/src/components/fundamental_list.vue'
import FundamentalDeep from '/src/components/fundamental_deep.vue'


const routes=[
  {
    path:'/',
    name:'Home',
    component: FundamentalList
  },
  {
    path:'/fundamental/:id',
    name:'FundamentalDeep',
    component: FundamentalDeep
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

