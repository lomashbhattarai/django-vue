<template>
    <component :is="loaderKind" primaryColor="#add8e6"/>
</template>

<script>
    import {
    ContentLoader,
    FacebookLoader,
    CodeLoader,
    BulletListLoader,
    InstagramLoader,
    ListLoader
    } from 'vue-content-loader'

    export default {
        name:'loader',
        components: {
            ContentLoader,
            FacebookLoader,
            CodeLoader,
            BulletListLoader,
            InstagramLoader,
            ListLoader
        },
        props:{
            kind:{
                type: String,
                default: 'BulletList'
            }
        },
        computed:{
            loaderKind(){
                return this.kind + 'Loader'
            }
        }
    }
</script>
