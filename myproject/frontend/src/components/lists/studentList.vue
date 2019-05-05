<template>
    <v-container>
        <v-layout>
            <v-flex xs6>
                <h2>Students</h2>
                <template v-if="!students.length">
                    <content-loader v-for="x in 4" kind="Facebook" :key="x"/>
                </template>
                <template v-else>
                        <v-list>
                            <v-list-tile
                                v-for="student in students"
                                :key="student.id"
                            >
                                <v-list-tile-avatar>
                                <img :src="student.profile_image">
                                </v-list-tile-avatar>

                                <v-list-tile-content>
                                <v-list-tile-title v-text="student.first_name+' '+student.last_name"></v-list-tile-title>
                                </v-list-tile-content>

                                <v-list-tile-action>
                                    <v-icon color="pink">star</v-icon>
                                </v-list-tile-action>


                                
                            </v-list-tile>
                        </v-list>
                </template>
            </v-flex>
        </v-layout>
    </v-container>    
</template>

<script>
import { mapState } from 'vuex'
export default {
    created(){
      this.$store.dispatch("teacher/getTeacherList")
    },
    data(){
        return {
            students :[]
        }
    },
    computed:{
        ...mapState('teacher',[
            'teachers'
        ])
        

    }
   
}
</script>

