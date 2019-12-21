<template>
    <!-- форма ввода данных для поискового запроса -->
  <div>
    <div class="q-pa-md" style="width: 800px">
        <div class="q-pa-md" style="font-size: 24px; color: dodgerblue">
          Задайте параметры поиска:
        </div>
        <div class="q-gutter-md">
            <q-input
                style = 'width: 720px'
                dense
                square
                outlined
                v-model="keywords"
                label="Ключевые слова"
                :rules="[ val => val && val.length > 0 || 'Please type something',
                        val => val.length <= 128 || 'Please use maximum 128 characters'
                        ]"
            />
        </div>
        <div class="q-gutter-md">
            <q-select
                style = 'width: 350px; display: inline-block'
                dense
                square
                outlined
                v-model="employment_type"
                :options="options_employment"
                label="Тип занятости"
            />
            <q-select
                style = 'width: 350px; display: inline-block'
                dense
                square
                outlined
                v-model="skill"
                :options="options_skill"
                label="Опыт работы"
            />
        </div>
        <div class="flex flex-center" style="margin-top: 40px">
            <q-btn @click="send" color="primary" label="Найти" style="width: 350px; height: 40px" />
        </div>
    </div>
    <br>
    <div class="q-pa-md">
      <q-table
        class="my-sticky-virtscroll-table"
        :dense="$q.screen.lt.md"
        title="Результат"
        table-style="max-height: 1200px"
        :data="data"
        :columns="columns"
        @row-click = 'link'
        :pagination.sync="pagination"
        :rows-per-page-options="[10]"
         :virtual-scroll-sticky-start="10"
        row-key="index"
      />
    </div>
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
          style: 'max-width: 3px'
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
        { name: 'company',
          align: 'left',
          label: 'Компания',
          field: 'company',
          sortable: true,
          classes: 'ellipsis',
          style: 'max-width: 200px'
        },
        { name: 'city',
          align: 'left',
          label: 'Город',
          field: 'city',
          sortable: true,
          style: 'max-width: 200px'
        },
        { name: 'date',
          align: 'left',
          label: 'Дата размещения',
          field: 'date',
          style: 'max-width: 50px'
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
            employment: this.employment_type.value
          }
        })
        .then((res) => {
          console.log('Ответ сервера:', res)
          this.data = res.data
          this.data.forEach((row, index) => {
            row.index = index
          })
        })
    },
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
