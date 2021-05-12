import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../components/Index'
import Handle from "../components/Handle";

Vue.use(VueRouter)

let router = new VueRouter({
    routes: [
        {
            path: '/',
            component: Index
        },
        {
            path: '/handle',
            component: Handle
        }
    ]
})

export default router