<template>
<q-card flat bordered class="my-card">
    <q-card-section>
      <div class="text-h6">Дорогие друзья!</div>
    </q-card-section>
      <q-card-section style="font-size: 16px">
          Данный ресурс посвящен поиску и сбору вакансий с разнообразных порталов
        о трудоустройстве в сети Интернет в соответствии с Вашим личным запросом.
          А также оповещении зарегистрированного на портале пользователя о том,
        что по его критериям запроса появились новые предложения о работе.
      </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'inform',

  data () {
    return {
      username: localStorage.user
    }
  }

}
</script>

<style scoped>

</style>
