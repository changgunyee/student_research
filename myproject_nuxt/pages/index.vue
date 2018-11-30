<template>
  <div>

    <input type="file" id="question_excel_file" ref="question_input" v-on:change="fileUpload()" required='true'/>

    <input type="file" id="answer_excel_file" ref="answer_input" v-on:change="fileUpload()" required='true'/>

    <button v-on:click="submitFiles()">Submit</button>

    <button v-on:click="select=1">응답결과</button>

    <button v-on:click="select=2">문항별 응답비율</button>

    <template v-if="select==1">
      <AnswerTable ></AnswerTable>
    </template>

    <template v-if="select==2">
      <AnswerRateTable></AnswerRateTable>
    </template>
      
  </div>
</template>
<script>
import axios from 'axios'
import AnswerTable from '~/components/AnswerTable.vue'
import AnswerRateTable from '~/components/AnswerRateTable.vue'
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
  },
  components:{
    AnswerTable,
    AnswerRateTable,
  }
}
</script>
<style>
table{
    white-space: nowrap;
    table-layout: fixed;
}
</style>
