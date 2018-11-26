<template>
  <div>

    <input type="file" id="question_excel_file" ref="question_input" v-on:change="fileUpload()" required='true'/>

    <input type="file" id="answer_excel_file" ref="answer_input" v-on:change="fileUpload()" required='true'/>

    <button v-on:click="submitFiles()">Submit</button>

    <button v-on:click="callAnswers()">응답결과</button>

    <button v-on:click="callAnswers2()">문항별 응답비율</button>
    
      <table>
        <tr>
          <th v-for="column in columns" :key="column.key">{{column}}</th>
        </tr>
        <div v-if="select==1">
          <person v-for="person in persons" :key="person.key" :name="person.name" :email="person.email" :answers="person.answers"></person>
        </div>
        <div v-else-if="select==2">
          <tr v-for="question in response_rate" :key="question.key">
            <th>{{question}}</th>
            <td v-for="column in columns" :key="column.key">
              {{question[column]}}
            </td>
          </tr>
        <div v-else>
        </div>
      </table>
    </div>  
</template>
  <!--<section class="container">
    <div>
      <app-logo/>
      <h1 class="title">
        myproject_nuxt
      </h1>
      <h2 class="subtitle">
        Nuxt.js project
      </h2>
      <div class="links" >
        <a
          href="https://nuxtjs.org/"
          target="_blank"
          class="button--green">Documentation</a>
        <a
          href="https://github.com/nuxt/nuxt.js"
          target="_blank"
          class="button--grey">GitHub</a>
      </div>
    </div>
  </section>-->
<script>
import axios from 'axios'
import Person from '~/components/Person.vue'
export default{
  data(){
    return {
      select:0,
      files: {},
      columns:[],
      persons:{},
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
    callAnswers(){
      this.select=1;
       const config ={
         'content-type':'application/json',
         headers:{
           'Access-Control-Request-Headers': '',
           },
       }
      return axios.get('http://54.180.115.81:8000/polls/person/0',config).then((response)=>{
        this.persons=response.data['persons']
        this.columns=response.data['columns']
      }).catch((e)=>{
        console.log(e);
      })
    },
    callAnswers2(){
      this.select=2;
      const config ={
         'content-type':'application/json',
         headers:{
           'Access-Control-Request-Headers': '',
           },
       }
       return axios.get('http://54.180.115.81:8000/polls/response_rate',config).then((response)=>{
        this.response_rate=response.data['response_rate']
        this.columns=reponse.data['columns']
      }).catch((e)=>{
        console.log(e)
      })
    }
  },
  components:{
    Person
  }
}
</script>
<style>
table{
    white-space: nowrap;
    table-layout: fixed;
}
</style>
