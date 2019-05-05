<template>
    <div>
        <h2>Teachers</h2>
        <template v-if="!teachers.length">
            <content-loader v-for="x in 4" kind="Facebook" :key="x"/>
        </template>
        <template v-else>
                <v-list>
                    <v-list-tile
                        v-for="teacher in teachers"
                        :key="teacher.id"
                    >
                        <v-list-tile-avatar>
                        <img :src="teacher.profile_image">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                        <v-list-tile-title v-text="teacher.first_name+' '+teacher.last_name"></v-list-tile-title>
                        </v-list-tile-content>

                        <v-list-tile-action>
                            <v-icon color="pink">star</v-icon>
                        </v-list-tile-action>


                        
                    </v-list-tile>
                </v-list>
        </template>
    </div>
               
</template>

<script>
import { mapState } from 'vuex'
export default {
    created(){
      this.$store.dispatch("teacher/getTeacherList")
    },
    computed:{
        ...mapState('teacher',[
            'teachers'
        ])
        

    }
   
}
</script>

