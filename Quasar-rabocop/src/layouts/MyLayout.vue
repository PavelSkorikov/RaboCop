<template>
  <q-layout view="lHh Lpr lFf">
    <!--    верхняя панель-->
    <q-header elevated>
      <q-toolbar>
        <img alt="RaboCop" src="~assets/logo-white.png" style="width: 30px">
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title>
          Поиск удаленной работы
        </q-toolbar-title>
<!--        меню авторизованного пользователя-->
        <div v-if="isAuth">
          {{ username }}
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
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
        <q-item clickable v-ripple to="/desktop">
          <q-item-section avatar>
            <q-icon name="assignment" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Мои запросы</q-item-label>
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
        <q-item v-if="noAuth" clickable to="/register">
          <q-item-section avatar>
            <q-icon name="assignment_ind" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Регистрация</q-item-label>
          </q-item-section>
        </q-item>
        <q-item v-if="noAuth" clickable to="/login">
          <q-item-section avatar>
            <q-icon name="account_circle" />
          </q-item-section>
          <q-item-section>
            <q-item-label>ВХОД</q-item-label>
            <q-item-label caption>войти в систему</q-item-label>
          </q-item-section>
        </q-item>
        <q-item v-if="isAuth" clickable @click="logout">
          <q-item-section avatar>
            <q-icon name="account_circle" />
          </q-item-section>
          <q-item-section>
            <q-item-label>ВЫЙТИ</q-item-label>
            <q-item-label caption>войти в систему</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
    <q-page-container style="margin: 10px">
      <q-page class="row">
        <div class="col-2"></div>
        <router-view class="col-8"/>
        <div class="col-2"></div>
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
