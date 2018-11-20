<template>
  <div>

    <input type="file" id="question_excel_file" ref="question_input" v-on:change="fileUpload()" required='true'/>

    <input type="file" id="answer_excel_file" ref="answer_input" v-on:change="fileUpload()" required='true'/>

    <button v-on:click="submitFiles()">Submit</button>

    <button v-on:click="callAnswers()">불러오기</button>

    <div v-for="person in persons" :key="person.key">
      <person :name="person.name" :email="person.email" :answers="person.answers"></person>
    </div>
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
      files: {},
      persons:{}
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
      return axios.get('http://localhost:8000/polls/person/0').then((response)=>{
        this.persons=response.data
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