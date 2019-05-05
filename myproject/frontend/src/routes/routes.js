import Dashboard from '../components/dashboard'
import LoginApp from '../components/auth/login'
const routes = [
    {
        path: '/',
        component: Dashboard
    },
    {
        path:'/login',
        component: LoginApp
    }
]

export default routes