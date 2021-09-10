<template>
  <h1>{{comp.header}} <sup>{{comp.sticker}}</sup></h1>
  <div сlass="row">
    <a href="" @click.prevent="show_fundamental=!show_fundamental">смотреть фундаментальные показатели</a>
    <div v-if="show_fundamental">
      <table class="table col-md-4">
        <thead>
          <tr>
            <th scope="col">Показатель</th>
            <th scope="col">Значение</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="(k,idx) in key_list_arr" :key="idx" class="hovered">
            <td>{{key_list[k].header}}<br>
              <small>{{key_list[k].body}}</small>
            </td>
            <td>{{comp_ratios[k]}}{{key_list[k].percent?'%':''}}</td>

          </tr>

        </tbody>

      </table>
    </div>

  </div>


  <div>

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
      show_fundamental: false,
      sticker:false,
      key_list:{},
      comp:{},
      comp_ratios:{},
      indicators:{},
      indicator_list: []
      
    }
  },
  created(){
    this.sticker=this.$route.params.sticker
    this.get()
  },
  computed:{
    key_list_arr(){
      let arr=[]
      for(let k in this.key_list){
        if(k!='header')
          arr.push(k)
      }
      return arr
    }
  },
  methods:{
    get(){
      httpGET({
        url:'/sticker/fundamental/'+this.sticker,
        success:(data)=>{
          this.comp=data.comp
          this.comp_ratios=data.comp_ratios,
          this.key_list=data.key_list
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
  tr.hovered:hover {background-color: #bebebe; }
</style>
