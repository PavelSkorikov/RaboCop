<template>
    <!-- форма регистрации нового пользователя -->
    <div class="q-pa-md">
        <div class="q-pa-md" style="font-size: 18px">Введите данные для регистрации:</div>
            <q-input
                square
                outlined
                v-model="user_data.username"
                label="Имя пользователя"
                :rules="[ val => val && val.length > 0 || 'Please type something',
                        val => val.length <= 20 || 'Please use maximum 20 characters'
                        ]"
            />
             <q-input
                square
                outlined
                v-model="user_data.email"
                label="Адрес электронной почты"
                filled type="email"
                :rules="[ val => val && val.length > 0 || 'Please type something']"
             />
            <q-input v-model="user_data.password"
                filled :type="isPwd ? 'password' : 'text'"
                label="Пароль"
                :rules="[ val => val && val.length > 0 || 'Please type something']">
            <template v-slot:append>
            <q-icon
                :name="isPwd ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd = !isPwd"
            />
            </template>
      </q-input>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn @click="send" color="primary" label="Отправить" style="width: 400px; height: 40px" />
        </div>
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
      isPwd: true
    }
  },
  methods: {
    send () {
      this.$axios.post(this.appConfig.auth_url + '/users/', this.$qs.stringify(this.user_data))
        .then((response) => {
          console.log(response.data)
          this.auth_user = response.data
        })
        .catch((error) => {
          alert(JSON.stringify(error.response.data))
        })
    }
  }
}
</script>
