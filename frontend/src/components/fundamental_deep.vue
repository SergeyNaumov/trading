<template>
  <h1>{{comp.header}} <sup>{{comp.sticker}}</sup></h1>
  <div class="row">
    <div class="col-md-4" v-for="(i,idx) in indicator_list" :key="idx">
      <LineDiagram :list="indicators[i.indicator]" v-if="indicators[i.indicator]" :description="i.header"/>
      
      
    </div>
  </div>  
  


</template>

<script>
import {httpGET} from '/src/javascript/fetch'
import LineDiagram from './fundamental_deep/line_diagram' 
export default {
  name: 'FundamentalDeep',
  components:{ LineDiagram },
  data(){
    return {
      id:false,

      comp:{},
      indicators:{},
      indicator_list: []
      
    }
  },
  created(){
    this.id=this.$route.params.id
    this.get()
  },
  methods:{
    get(){
      httpGET({
        url:'/sticker/fundamental/'+this.id,
        success:(data)=>{
          this.comp=data.comp
          this.indicators=data.indicators
          this.indicator_list=data.indicator_list
          document.title=`${this.comp.header} - фундаментальные показатели`
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
