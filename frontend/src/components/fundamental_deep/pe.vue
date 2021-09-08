<template>
    
    <LineDiagram :list="list" v-if="list.length" description="p/e"/>


    
</template>
<script>





import LineDiagram from './line_diagram' 
export default {
    name:'pe',
    props:['list'],
    components:{LineDiagram},
    created(){
        
        




    },
    
    data(){
        return {
            labels:[],
            values:[],
            width: 500,
            height:300,
            id: ''
        }
    },
    methods: {


    }
}
</script>
<style scoped>
</style>