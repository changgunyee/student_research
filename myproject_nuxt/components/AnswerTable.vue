<template>
    <table> 
        <tr>
            <th v-for="column in columns" :key="column.key">
                {{column}}
            </th>
        </tr>
        <tr v-for="person in persons" :key="person.key">
            <th>{{person.name}}</th>
            <td>{{person.email}}</td>
            <td v-for="answer in person.answers" :key="answer.key"> {{answer}}</td>
        </tr>
    </table>
</template>
<script>
import axios from 'axios'
export default{
  data(){
      columns=[]
      persons={}
      const config ={
         'content-type':'application/json',
         headers:{
           'Access-Control-Request-Headers': '',
           },
       }
      axios.get('http://54.180.115.81:8000/polls/person/0',config).then((response)=>{
        this.persons=response.data['persons']
        this.columns=response.data['columns']
      }).catch((e)=>{
        console.log(e);
      })
    return {
        columns,
        persons,
    }
  },
}
</script>