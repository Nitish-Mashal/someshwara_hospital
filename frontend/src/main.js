import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

// Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// ✅ ADD THIS LINE
import 'bootstrap-icons/font/bootstrap-icons.css'

// Element Plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(ElementPlus)
app.use(resourcesPlugin)

app.component('Button', Button)
app.mount('#app')