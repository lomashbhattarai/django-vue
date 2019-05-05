<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>School</span>
        <span class="font-weight-light">Managment System</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">In development</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view />
      <!-- <dashboard/> -->
    </v-content>
  </v-app>
</template>

<script>
import dashboard from './components/dashboard'

export default {
  name: 'App',
  components: {
    dashboard
  },
  data () {
    return {
      //
    }
  }
}
</script>
