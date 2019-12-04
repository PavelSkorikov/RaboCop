import Vue from 'vue'
import axios from 'axios'
const config = require('../config')

// экспортируем алиас $axios для доступа из любого компонента
Vue.prototype.$axios = axios
// экспортируем наш конфиг appConfig для доступа из любого компонента
Vue.prototype.appConfig = config
