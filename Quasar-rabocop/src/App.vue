<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  created: function () {
    this.$axios.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
        // если сервер возвращает ошибку авторизации (токен просрочен), выполняем логаут пользователя
          localStorage.removeItem('token')
          localStorage.removeItem('user')
          // удаляем токен из заголовка авторизации
          delete this.$axios.defaults.headers.common['Authorization']
          //  переходим на главную страницу
          document.location.href = this.appConfig.main_page
        }
        throw err
      })
    })
  }
}
</script>
