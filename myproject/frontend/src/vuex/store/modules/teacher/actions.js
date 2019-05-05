import axios from 'axios'


const actions = {
    getTeacherList({commit}){
        return axios.get('http://localhost:8000/teachers/').then(({data}) =>{
            commit('getTeacherList',data)
        })
        
    }    
}

export default actions