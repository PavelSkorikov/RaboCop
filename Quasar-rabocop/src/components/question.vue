<template>
    <!-- форма ввода данных для поискового запроса -->
    <div class="q-pa-md" style="width: 350px">
        <div class="q-pa-md" style="font-size: 24px; color: dodgerblue">Форма поиска:</div>
        <div class="q-gutter-md">
            <q-input
                square
                outlined
                v-model="keywords"
                label="Ключевые слова"
                :rules="[ val => val && val.length > 0 || 'Please type something',
                        val => val.length <= 128 || 'Please use maximum 128 characters'
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
                v-model="employment_type"
                :options="options_employment"
                label="Тип занятости"
            />
        </div>
        <br>
        <div class="q-gutter-md">
            <q-select
                square
                outlined
                v-model="schedule_work"
                :options="options_schedule"
                label="График работы"
            />
        </div>
         <div class="q-pa-lg">
            <q-option-group
            v-model="skill"
            :options="options_skill"
            color="primary"
            inline
            />
        </div>
        <div class="q-gutter-sm">
            <q-checkbox left-label v-model="remote" label="Хочу работать удаленно" />
        </div>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn @click="send" color="primary" label="Отправить" style="width: 350px; height: 40px" />
        </div>
    </div>
</template>

<script>
export default {
  name: 'question',
  data () {
    return {
      employment_type: '',
      schedule_work: '',
      remote: false,
      keywords: '',
      location: '',
      skill: true,
      options_skill: [
        {
          label: 'Есть опыт работы',
          value: true
        },
        {
          label: 'Нет опыта',
          value: false
        }
      ],
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
          value: 'INTERN'
        }
      ],
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
          value: 'REMOTE'
        }
      ]
    }
  },
  methods: {
    send () {
      let postdata = {
        keywords: this.keywords,
        remote: this.remote,
        location: this.location,
        skill: this.skill,
        employment: this.employment_type.value,
        schedule_work: this.schedule_work.value
      }
      this.$axios.post(this.appConfig.api_url + 'question/create/', this.$qs.stringify(postdata)).then((res) => {
        console.log('Ответ сервера:', res)
      })
    }
  }
}
</script>
