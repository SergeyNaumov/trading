<template>
  <h1>{{comp.header}} <sup>{{comp.sticker}}</sup></h1>
  <div>
    <a :href="'https://smart-lab.ru/gr/MOEX.'+comp.sticker" target="_blank">Онлайн-график</a>
  </div>
  <div class="row">
    <template v-for="(i,idx) in indicator_list">
    <div class="col-md-4"  :key="idx" v-if="indicators[i.indicator]">
      <LineDiagram :list="indicators[i.indicator]"  :description="i.header"/>
      
      
    </div>
    </template>
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
