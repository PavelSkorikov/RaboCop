<template>
<h5>Здравствуйте, {{ username }}</h5>
</template>

<script>
export default {
  name: 'desktop',

  data () {
    return {
      username: localStorage.user
    }
  }

}
</script>

<style scoped>

</style>
