<!-- страница регистрации нового пользователя -->
<template>
    <div class="q-pa-md flex flex-center">
      <!-- форма входа пользователя -->
      <q-form
        @submit="send"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="q-pa-md" style="font-size: 24px; color: dodgerblue">Введите Ваши данные:</div>
            <q-input
                square
                outlined
                v-model="user_data.username"
                style="max-width: 400px"
                label="Имя пользователя"
                :rules="[ val => val && val.length > 0 || 'Пожалуйста введите Ваше имя',
                        val => val.length <= 20 || 'Имя не должно превышать 20 символов'
                        ]">
                <template v-slot:before>
                  <q-icon name="account_box" />
                </template>
            </q-input>
            <q-input
                v-model="user_data.password"
                style="max-width: 400px"
                filled :type="isPwd ? 'password' : 'text'"
                label="Пароль"
                :rules="[ val => val && val.length > 0 || 'Пожалуйста введите пароль']">
                <template v-slot:before>
                  <q-icon name="vpn_key" />
                </template>
                <template v-slot:append>
                <q-icon
                    :name="isPwd ? 'visibility_off' : 'visibility'"
                    class="cursor-pointer"
                    @click="isPwd = !isPwd"
                />
                </template>
            </q-input>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn type="submit" color="primary" label="Войти" style="width: 200px; height: 40px" />
            <q-btn label="сброс" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>
    </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      user_data: {
        username: '',
        password: ''
      },
      auth_user: {},
      isPwd: true,
      err_message: ''
    }
  },
  methods: {
    // метод отправки формы на сервер
    send () {
      this.$axios.post(this.appConfig.auth_url + '/token/login/', this.$qs.stringify(this.user_data))
        .then((response) => {
          localStorage.token = response.data.auth_token
          localStorage.user = this.user_data.username
          this.$axios.defaults.headers.common = {
            'Authorization': 'Token ' + localStorage.token
          }
          document.location.href = this.appConfig.main_page
        })
        .catch((error) => {
          if (error.response.data.non_field_errors) {
            this.err_message = error.response.data.non_field_errors[0]
          }
          this.$q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: this.err_message
          })
        })
    },
    // метод сброса данных формы
    onReset () {
      this.user_data.username = ''
      this.user_data.password = ''
    }
  }
}
</script>
