import actions from './actions'
import state from './state'
import getters from './getters'
import mutations from './mutations'

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
}

