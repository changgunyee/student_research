<template>
  <div>
    <input type="hidden" name="_token" :value="csrf">

    <input type="file" id="question_excel_file" ref="question_input" v-on:change="fileUpload()" required='true'/>

    <input type="file" id="answer_excel_file" ref="answer_input" v-on:change="fileUpload()" required='true'/>

    <button v-on:click="submitFiles()">Submit</button>
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
export default{
  data(){
    let files={}
    return files
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
      return axios.post('https://127.0.0.1:8000/polls/upload',data,config).then((e)=>{
          console.log(e)
      })
    }
  }
}
</script>