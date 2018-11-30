<template>
  <div>

    <input type="file" id="question_excel_file" ref="question_input" v-on:change="fileUpload()" required='true'/>

    <input type="file" id="answer_excel_file" ref="answer_input" v-on:change="fileUpload()" required='true'/>

    <button v-on:click="submitFiles()">Submit</button>

    <button v-on:click="select=1">응답결과</button>

    <button v-on:click="select=2">문항별 응답비율</button>
      
          <AnswerTable v-if="select==1"></AnswerTable>
     <!--<table>
         <tr>
            <th v-for="column in columns" :key="column.key">{{column}}</th>
         </tr>
        <person v-for="person in persons" :key="person.key" :name="person.name" :email="person.email" :answers="person.answers"></person>
        </table>
        <template v-else-if="select==2">
          <table>
          <tr>
            <th></th>
            <th v-for="column in columns" :key="column.key">{{column}}</th>
          </tr>
          <tr v-for="(question,key) in response_rate" :key="question.key">
            <th>{{key}}</th>
            <td v-for="column in columns" :key="column.key">
              {{question[column]}}
            </td>
          </tr>
        </table>-->  
</template>
<script>
import axios from 'axios'
import AnswerTable from '~/components/AnswerTable.vue'
export default{
  data(){
    return {
      select:0,
      files: {},
      columns:[],
      response_rate:{},
    }
  },
  methods:{
    fileUpload(){
      this.files={
        "question_excel_file":this.$refs.question_input.files[0],
        "answer_excel_file":this.$refs.answer_input.files[0]
      }
    },
    submitFiles(){
      let data= new FormData()

      data.append("question_excel_file",this.files["question_excel_file"])
      data.append("answer_excel_file",this.files["answer_excel_file"])

      const config = {
            headers: { 
              'content-type': 'multipart/form-data'
            }
        }
      return axios.post('http://54.180.115.81:8000/polls/upload',data,config).then((e)=>{
        console.log(e)
      }).catch((e)=>{
        console.log(e)
      })
    },

    callAnswers2(){
      this.columns=[]
      this.select=2
      const config ={
         'content-type':'application/json',
         headers:{
           'Access-Control-Request-Headers': '',
           },
       }
       return axios.get('http://54.180.115.81:8000/polls/response_rate',config).then((response)=>{
        this.response_rate=response.data['response_rate']
        this.columns=response.data['columns']
      }).catch((e)=>{
        console.log(e)
      })
    }
  },
  components:{
    AnswerTable,
  }
}
</script>
<style>
table{
    white-space: nowrap;
    table-layout: fixed;
}
</style>
