<template>
    <!-- форма ввода данных для поискового запроса -->
    <div class="q-pa-md" style="width: 800px">
        <div class="q-pa-md" style="font-size: 24px; color: dodgerblue">Задайте параметры поиска:</div>
        <div class="q-gutter-md">
            <q-input
                style = 'width: 350px; display: inline-block'
                square
                outlined
                v-model="keywords"
                label="Ключевые слова"
                :rules="[ val => val && val.length > 0 || 'Please type something',
                        val => val.length <= 128 || 'Please use maximum 128 characters'
                        ]"
            />
            <q-select
                style = 'width: 350px; display: inline-block'
                square
                outlined
                v-model="skill"
                :options="options_skill"
                label="Опыт работы"
            />
        </div>
         <br>
        <div class="q-gutter-md">
            <q-select
                style = 'width: 350px; display: inline-block'
                square
                outlined
                v-model="employment_type"
                :options="options_employment"
                label="Тип занятости"
            />
            <q-select
                style = 'width: 350px; display: inline-block'
                square
                outlined
                v-model="schedule_work"
                :options="options_schedule"
                label="График работы"
            />
        </div>
        <br>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn @click="send" color="primary" label="Отправить" style="width: 350px; height: 40px" />
        </div>
      <br><br><br><br>
       <div class="q-pa-md" style="width: 1150px">
        <q-table
          title="hh.ru"
          :data="data"
          :columns="columns"
          row-key="name"
          selection="single"
          :selected.sync="selected"
        />
        <div class="q-mt-md">
          Selected: {{ JSON.stringify(selected) }}
        </div>
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
      keywords: '',
      skill: '',
      options_skill: [
        {
          label: 'Есть опыт',
          value: 'doesNotMatter'
        },
        {
          label: 'Нет опыта',
          value: 'noExperience'
        }
      ],
      options_employment: [
        {
          label: 'Не важно',
          value: ''
        },
        {
          label: 'Полная занятость',
          value: 'full'
        },
        {
          label: 'Частичная занятость',
          value: 'part'
        },
        {
          label: 'Временная работа',
          value: 'project'
        },
        {
          label: 'Стажировка',
          value: 'probation'
        }
      ],
      options_schedule: [
        {
          label: 'Не важно',
          value: ''
        },
        {
          label: 'Полный день',
          value: 'fullDay'
        },
        {
          label: 'Сменный график',
          value: 'shift'
        },
        {
          label: 'Гибкий график',
          value: 'flexible'
        },
        {
          label: 'Вахтовый метод',
          value: 'flyInFly'
        }
      ],
      selected: [],
      columns: [
        {
          name: 'name',
          required: true,
          label: 'Описание',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'company', align: 'left', label: 'Компания', field: 'company', sortable: true },
        { name: 'city', align: 'left', label: 'Город', field: 'city', sortable: true },
        { name: 'date', align: 'left', label: 'Дата размещения', field: 'date', sortable: true },
        { name: 'href', align: 'left', label: 'Ссылка', field: 'href' }
      ],
      data: []
    }
  },
  methods: {
    send () {
      this.$axios.get(this.appConfig.api_url + 'vacancy/list/',
        {
          params: {
            keywords: this.keywords,
            skill: this.skill,
            employment: this.employment_type.value,
            schedule_work: this.schedule_work.value
          }
        })
        .then((res) => {
          console.log('Ответ сервера:', res)
          this.data = res.data
        })
    }
  }
}
</script>
