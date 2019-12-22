<template>
    <!-- форма ввода данных для поискового запроса -->
  <div class="q-pa-md">
    <q-form
        @submit="send"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="q-pa-md" style="font-size: 24px; color: dodgerblue">
          Задайте параметры поиска:
        </div>
      <div class="row">
        <div class="col-md-6 col-xs-12">
          <q-input
              style = 'width: 350px'
              dense
              square
              outlined
              v-model="keywords"
              label="Ключевые слова"
              :rules="[ val => val && val.length > 0 || 'Please type something',
                      val => val.length <= 128 || 'Please use maximum 128 characters'
                      ]"
          />
          <q-select
              style = 'width: 350px'
              dense
              square
              outlined
              v-model="employment_type"
              :options="options_employment"
              label="Тип занятости"
          />
          <br>
          <q-select
              style = 'width: 350px'
              dense
              square
              outlined
              v-model="skill"
              :options="options_skill"
              label="Опыт работы"
          />
        </div>
        <div class="col-md-6 col-xs-12">
          <div class="q-gutter-sm">
            <q-checkbox v-model="saveQuery" label="Сохранить данный запрос" />
          </div>
          <div class="q-gutter-sm">
            <q-checkbox v-model="notification" label="Включить оповещение о новых вакансиях по e-Mail" />
          </div>
        </div>
      </div>
        <div class="flex flex-center" style="margin-top: 40px">
          <q-btn type="submit" v-if="!isQuery" color="primary" label="Найти" style="width: 350px; height: 40px" />
          <q-btn label="сброс" v-if="!isQuery" type="reset" color="primary" flat class="q-ml-sm" />
             <q-circular-progress
                v-if="isQuery"
                indeterminate
                size="50px"
                :thickness="1"
                color="blue"
                center-color="grey-8"
                class="q-ma-md"
              />
        </div>
    </q-form>
    <br><br>
    <q-table
      class="my-sticky-virtscroll-table"
      :dense="$q.screen.lt.md"
      :title= numberVacancies
      table-style="max-height: 400px"
      :data="data"
      :columns="columns"
      @row-click = 'link'
      :pagination.sync="pagination"
      :rows-per-page-options="[0]"
      row-key="index"
    />
  </div>
</template>

<script>
export default {
  name: 'question',
  data () {
    return {
      employment_type: '',
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
      selected: [],
      columns: [
        {
          name: 'index',
          label: '#',
          field: 'index',
          sortable: true,
          style: 'max-width: 2px'
        },
        {
          name: 'name',
          required: true,
          label: 'Вакансия',
          align: 'left',
          field: row => row.name,
          sortable: true,
          classes: 'bg-grey-2 ellipsis',
          style: 'max-width: 300px'
        },
        { name: 'compensation',
          align: 'left',
          label: 'Оплата',
          field: 'compensation',
          sortable: true,
          classes: 'ellipsis',
          style: 'max-width: 20px'
        },
        { name: 'company',
          align: 'left',
          label: 'Компания',
          field: 'company',
          sortable: true,
          classes: 'ellipsis',
          style: 'max-width: 100px'
        },
        { name: 'city',
          align: 'left',
          label: 'Город',
          field: 'city',
          sortable: true,
          classes: 'ellipsis',
          style: 'max-width: 50px'
        },
        { name: 'date',
          align: 'left',
          label: 'Размещено',
          field: 'date',
          style: 'max-width: 20px'
        },
        { name: 'source',
          align: 'left',
          label: 'Источник',
          field: 'source',
          sortable: true,
          style: 'max-width: 100px'
        }
      ],
      pagination: {
        rowsPerPage: 0
      },
      isQuery: false,
      saveQuery: false,
      notification: false,
      data: []
    }
  },
  computed: {
    numberVacancies: function () {
      let str = 'Найдено: ' + String(this.data.length)
      return str
    }
  },
  methods: {
    send () {
      this.isQuery = true
      this.$axios.get(this.appConfig.api_url + 'vacancy/list/',
        {
          params: {
            keywords: this.keywords,
            skill: this.skill,
            employment: this.employment_type.value
          }
        })
        .then((res) => {
          console.log('Ответ сервера:', res)
          this.data = res.data
          this.data.forEach((row, index) => {
            row.index = index
          })
          this.isQuery = false
        })
    },
    // метод сброса данных формы
    onReset () {
      this.keywords = ''
      this.skill = ''
      this.employment_type = ''
    },
    // метод перехода по ссылке
    link (evt, row) {
      window.open(row.href)
    }
  }
}
</script>

<style lang="sass">
  .my-sticky-virtscroll-table
  /* max height is important */
  .q-table__middle
    max-height: 1200px

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th /* bg color is important for th; just specify one */
    background-color: #fff

  thead tr:first-child th
    position: sticky
    font-size: 14px
    color: white
    background-color: #027BE3
    top: 0
    opacity: 1
    z-index: 1
</style>
