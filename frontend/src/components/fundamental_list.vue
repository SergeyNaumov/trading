<template>
  <div>
    <h1>Поиск акций</h1>
    <small>
      <a href="" @click.prevent="show_cols=!show_cols">вкл / выкл столбцы</a> |
      <a href="" @click.prevent="show_search=!show_search">поиск по параметрам</a>
    </small>
    <div class="row show_cols" v-if="show_cols"> 
      <div class="col-md-2" v-for="k in key_list" :key="k">
        <input type="checkbox" v-model="k.on" @change="gen_list_sorted"> {{k.header}}
      </div>
    </div>
    
    <div v-if="show_search" class="row show_search">
      <div class="col-md-4" >
          Наименование:<br><input type="text" class="form_control" v-model="search_filter.header" @keyup="gen_list_sorted">
      </div>
      <div class="col-md-8" >
        P/E:<br>
        <input type="number" class="form_control" v-model="search_filter.pe[0]" @keyup="gen_list_sorted">  - 
        <input type="number" class="form_control" v-model="search_filter.pe[1]" @keyup="gen_list_sorted">
        {{search_filter.pe}}
      </div>
    </div>

    <table class="table">
      <thead>
        <tr>
          <th scope="col" v-for="(h,idx) in header_list" :key="h">
            <a href="" @click.prevent="set_sort(idx)">{{h.header}}</a>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(c,idx) in list_sorted" :key="c.id" >
            <td v-for="(v,jdx) in c" :key="idx+jdx" :style="dynamic_style(v,jdx)" v-html="v" />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {httpGET} from '/src/javascript/fetch'
import {key_list} from './key_list'
import {search_param_ok, dynamic_style} from './filter_functions'

export default {
  name: 'fundamental_list',
  props: {
    
  },
  data(){
    return {
      text_filter:'',
      sort: 0, // sort -- номер столбца
      sort_desc:false,
      show_cols: false,
      key_list: key_list,
      list:[],
      list_sorted:[],
      show_search:false,
      search_filter:{
        header:'',
        pe:['0.0001','10'],
        ps:['',''],
        pb:['',''],
      }
    }
  },
  created(){
    this.get()
  },
  methods:{
    get(){
      httpGET({
        url: '/sticker/list',
        success: (data)=>{
          this.list=data
          this.gen_list_sorted()
        },
        errors: this.errors

      })
    },
    dynamic_style(v,jdx){ // если параметр отстойный -- подсвечиваем красным, иначе зелёным
      let name=this.getSortKey(jdx)
      
      
      return dynamic_style(name,v)
    },
    get_td_values(c){ // собираем в строку только те данные, которые выбраны
      let td_values=[]
      for(let k in this.key_list){
        if(this.key_list[k].on){
          if(k=='header'){
            td_values.push(`<a href="https://smart-lab.ru${c['fundamental_link']}" target="_blank">${c[k]}</a>`)
          }
          else{
            td_values.push(c[k])
          }
          
        }
      }
      return td_values
    },

    set_sort(v){
      if(this.sort==v){
        this.sort_desc=!this.sort_desc
      }
      else{
        this.sort=v
        this.sort_desc=false
      }
      
      this.gen_list_sorted()
    },
    getSortKey(sort){ // по номеру столбца получаем имя
      let idx=0;
      for(let k in this.key_list){
        if(this.key_list[k].on){
          if(sort==idx){
            return k
          }
          idx++
        }
      }
    },

    gen_list_sorted(){
      
      let list=[]
      let SF=this.search_filter
      for(let c of this.list){

        if(search_param_ok(c,SF)){
      
          list.push(this.get_td_values(c))
        }
      }
      let sort=this.sort
      list.sort(
        (a,b)=>{
         // console.log(sort,a)
          let asrt=a[sort]
          let bsrt=b[sort]
          if(this.getSortKey(sort) in ['header','sticker']){ // если это header или стикер -- сортируем как строку
            asrt=asrt.toLowerCase()
            bsrt=bsrt.toLowerCase()
          }
          if(this.sort_desc){

            return (asrt>bsrt)?1:-1
          }
          else{
            return (asrt>bsrt)?-1:1
          }

        }
      )
      // console.log(list)
      this.list_sorted=list
      
    }
  },
  computed:{
    header_list(){
      let list=[]
      for(let k in this.key_list){
        if(this.key_list[k].on){
          list.push({header:this.key_list[k].header,name:k})
        }
      }
      return list
    },
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .show_cols {border: 1px solid gray; font-size: 0.7rem; border-radius: 5px; margin-bottom: 10px; padding: 10px;}
  table th {vertical-align: top;}
  table th, table td {font-size: 0.7rem;}
</style>
