<template>
    <div>
        <table>
            <tr>
                <th></th>
                <th v-for="column in columns" :key="column.key">{{column}}</th>
            </tr>
            <tr v-for="(question,key) in answer_rate" :key="question.key">
                <th>{{key}}</th>
                <td v-for="column in columns" :key="column.key">
                {{question[column]}}
                </td>
            </tr>
        </table>
        <Pagination :count_data="count"></Pagination>
    </div>
</template>
<script>
import axios from 'axios'
import Pagination from '~/components/Pagination.vue'
export default{
  data(){
    return {
      columns:[],
      answer_rate:{},
      count:0,
    }
  },
  created(){
      this.getAnswerRateData()
      this.count=Object.keys(this.answer_rate).length;
  },
  methods:{
    getAnswerRateData(){
      const config ={
         'content-type':'application/json',
         headers:{
           'Access-Control-Request-Headers': '',
           },
       }
       return axios.get('http://54.180.115.81:8000/polls/answer_rate',config).then((response)=>{
        this.answer_rate=response.data['answer_rate']
        this.columns=response.data['columns']
      }).catch((e)=>{
        console.log(e)
      })
    }
  },
}
</script>