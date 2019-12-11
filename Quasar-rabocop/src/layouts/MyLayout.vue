<template>
  <q-layout view="lHh Lpr lFf">
    <!--    верхняя панель-->
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title>
          Поиск работы
        </q-toolbar-title>
<!--    кнопки регистрации и авторизации-->
        <q-btn v-if="noAuth" flat size='md' color='white' label='Регистрация' to="/register" />
        <q-btn v-if="noAuth" flat color='white' label='Вход' to="/login" />
<!--        меню авторизованного пользователя-->
         <q-btn v-if="isAuth" color="primary" :label="username">
        <q-menu>
          <q-list style="min-width: 100px">
            <q-item clickable v-close-popup>
              <q-item-section>Личный кабинет</q-item-section>
            </q-item>
            <q-item clickable v-close-popup @click="logout">
              <q-item-section>Выход</q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-2"
    >
      <q-list>
        <q-item-label header>Меню</q-item-label>
        <q-item clickable v-ripple to="/">
          <q-item-section avatar>
            <q-icon name="account_balance" />
          </q-item-section>
          <q-item-section>
            <q-item-label>На главную</q-item-label>
            <q-item-label caption>перейти на главную страницу</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/question">
          <q-item-section avatar>
            <q-icon name="search" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Найти</q-item-label>
            <q-item-label caption>форма быстрого поиска</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://chat.quasar.dev">
          <q-item-section avatar>
            <q-icon name="account_box" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Личный кабинет</q-item-label>
            <q-item-label caption>для зарегистрированных пользователей</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://forum.quasar.dev">
          <q-item-section avatar>
            <q-icon name="record_voice_over" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Forum</q-item-label>
            <q-item-label caption>forum.quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://twitter.quasar.dev">
          <q-item-section avatar>
            <q-icon name="rss_feed" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Twitter</q-item-label>
            <q-item-label caption>@quasarframework</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" target="_blank" href="https://facebook.quasar.dev">
          <q-item-section avatar>
            <q-icon name="public" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Facebook</q-item-label>
            <q-item-label caption>@QuasarFramework</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
    <q-page-container style="margin: 20px">
      <q-page class="row">
       <div class="col-xs-12 col-sm-8 col-md-8 row justify-center">
        <router-view />
       </div>
       <div class="col-xs-12 col-sm-10 col-md-4">
          <img alt="RaboCop" src="~assets/logo.png" style="width: 300px">
        </div>
    </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'MyLayout',

  data () {
    return {
      leftDrawerOpen: false,
      username: localStorage.user,
      noAuth: !localStorage.user,
      isAuth: localStorage.user
    }
  },
  methods: {
    // метод логаута пользователя
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      // удаляем токен из заголовка авторизации
      delete this.$axios.defaults.headers.common['Authorization']
      //  переходим на главную страницу
      document.location.href = this.appConfig.main_page
    }
  }
}
</script>
