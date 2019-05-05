<template>
    <v-container>
        <v-layout>
            <v-flex xs6>
              <teacher-list></teacher-list>
            </v-flex>
            <v-flex xs6>
              <student-list></student-list>
            </v-flex>
        </v-layout>
  </v-container>
</template>

<script>
  import teacherList  from './lists/teacherList'
  import studentList  from './lists/studentList'
  export default {
    components:{
      teacherList,
      studentList,
    },
    
  }
</script>

