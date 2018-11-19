<template>
  <form action="54.180.115.81:8000/polls/upload" method="post" enctype="multipart/form-data">
  
    <input type="file" title="Upload question excel file" name="question_excel_file" required="required">

    <input type="file" title="Upload answer excel file" name="answer_excel_file" required="required">

    <input type="submit" value="Upload" style="border: 1px solid green; padding:5px; border-radius: 2px; cursor: pointer;">
  </form>
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
</template>
