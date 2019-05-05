import Vue from 'vue'
import Vuex from 'vuex'
import teacher from './modules/teacher/index'

Vue.use(Vuex)
export default new Vuex.Store({
    modules : {
        teacher
    }    
})