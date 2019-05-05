import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import store from './vuex/store/index'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'
import VueRouter from 'vue-router'
import routes from './routes/routes'

const requireComponent = require.context(
  './components/common',
  false,
  /[A-Z]\w+\.(vue|js)$/
)
requireComponent.keys().forEach(fileName => {
  const componentConfig = requireComponent(fileName)
  const componentName = upperFirst(
    camelCase(
      fileName
        .split('/')
        .pop()
        .replace(/\.\w+$/,'')

    )
  )
  Vue.component(
    componentName,
    componentConfig.default || componentConfig
  )

}) 

Vue.use(VueRouter) 
const router = new VueRouter({routes})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
