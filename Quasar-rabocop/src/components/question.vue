<template>
    <!-- форма ввода данных для поискового запроса -->
    <div class="q-pa-md" style="width: 450px">
        <h4>Данные для поиска</h4>
        <div class="q-gutter-md">
            <q-input
                square
                outlined
                v-model="keywords"
                label="Ключевые слова"
                :rules="[ val => val && val.length > 0 || 'Please type something',
                        val => val.length <= 128 || 'Please use maximum 3 characters'
                        ]"
            />
        </div>
        <br>
        <div class="q-gutter-md">
             <q-input
                square
                outlined
                v-model="location"
                label="Желаемое расположение"
                :rules="[ val => val && val.length > 0 || 'Please type something']"
             />
        </div>
         <br>
        <div class="q-gutter-md">
            <q-select
                square
                outlined
                v-model="employment"
                :options="options_employment"
                label="Тип занятости"
            />
        </div>
        <br>
        <div class="q-gutter-md">
            <q-select
                square
                outlined
                v-model="schedule"
                :options="options_schedule"
                label="График работы"
            />
        </div>
         <div class="q-pa-lg">
            <q-option-group
            v-model="group"
            :options="options_skill"
            color="primary"
            inline
            />
        </div>
        <div class="q-gutter-sm">
            <q-checkbox left-label v-model="remote" label="Хочу работать удаленно" />
        </div>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn @click="send" color="primary" label="Отправить" style="width: 450px; height: 40px" />
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      group: 'op1',
      options_skill: [
        {
          label: 'Есть опыт работы',
          value: 'op1'
        },
        {
          label: 'Нет опыта',
          value: 'op2'
        }
      ],
      employment: '',
      options_employment: [
        {
          label: 'Не знаю',
          value: 'NO'
        },
        {
          label: 'Полная занятость',
          value: 'FULL'
        },
        {
          label: 'Частичная занятость',
          value: 'PARTIAL'
        },
        {
          label: 'Временная работа',
          value: 'TEMPORARY'
        },
        {
          label: 'Стажировка',
          val: 'INTERN'
        }
      ],
      schedule: '',
      options_schedule: [
        {
          label: 'Не знаю',
          value: 'NO'
        },
        {
          label: 'Полный день',
          value: 'FULL'
        },
        {
          label: 'Сменный график',
          value: 'SHIFT'
        },
        {
          label: 'Гибкий график',
          value: 'FLEX'
        },
        {
          label: 'Вахтовый метод',
          val: 'REMOTE'
        }
      ],
      remote: false,
      keywords: '',
      location: ''
    }
  }
  // mounted() {
  //     this.$axios
  //       .get(this.appConfig.admin_url + '/getCategory')
  //       .then(response => (this.categories = response.data));
  //   },
}
</script>
