<!-- страница регистрации нового пользователя -->
<template>
    <div class="q-pa-md">
      <!-- форма регистрации нового пользователя -->
      <q-form
        @submit="send"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="q-pa-md" style="font-size: 18px">Введите данные для регистрации:</div>
            <q-input
                square
                outlined
                v-model="user_data.username"
                label="Имя пользователя"
                :rules="[ val => val && val.length > 0 || 'Пожалуйста введите Ваше имя',
                        val => val.length <= 20 || 'Имя не должно превышать 20 символов'
                        ]">
                <template v-slot:before>
                  <q-icon name="account_box" />
                </template>
            </q-input>
             <q-input
                square
                outlined
                v-model="user_data.email"
                type="email"
                label="Адрес электронной почты"
                filled
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Пожалуйста введите e-mail']">
                <template v-slot:before>
                  <q-icon name="mail" />
                </template>
             </q-input>
            <q-input v-model="user_data.password"
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
        <div class="flex flex-end" style="margin-top: 40px">
            <q-btn type="submit" color="primary" label="Отправить" style="width: 400px; height: 40px" />
            <q-btn label="сброс" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>
    </div>
</template>

<script>
export default {
  name: 'register',
  data () {
    return {
      user_data: {
        username: '',
        email: '',
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
      this.$axios.post(this.appConfig.auth_url + '/users/', this.$qs.stringify(this.user_data))
        .then((response) => {
          console.log(response.data)
          this.auth_user = response.data
          this.user_data = {}
          this.$router.push('/')
        })
        .catch((error) => {
          if (error.response.data.username) {
            this.err_message = error.response.data.username[0]
          }
          if (error.response.data.password) {
            this.err_message = error.response.data.password[0]
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
      this.user_data.email = ''
      this.user_data.password = ''
      this.accept = false
    }
  }
}
</script>
