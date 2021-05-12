import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from './route'

Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router: VueRouter,
  render: h => h(App),
}).$mount('#app')
