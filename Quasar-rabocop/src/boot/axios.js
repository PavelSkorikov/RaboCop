import Vue from 'vue'
import axios from 'axios'
import qs from 'qs'
const config = require('../config')

// устанавливаем токен в заголовок авторизации для всех исходящих запросов
const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common = {
    'Authorization': 'Token ' + token
  }
}

// экспортируем алиас $axios для доступа из любого компонента
Vue.prototype.$axios = axios.create({ headers: {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json, text/plain, */*'
} })

// экспортируем алиас $qs для доступа к модулю qs из любого компонента
// qs это модуль формирования JSON данных для передачи из axios
Vue.prototype.$qs = qs

// экспортируем наш конфиг appConfig для доступа из любого компонента
Vue.prototype.appConfig = config
