<template>
    <div>
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
        <Pagination :count="numOfPage"></Pagination>
    </div>
</template>
<script>
import axios from 'axios'
import Pagination from '~/components/Pagination.vue'
export default{
  data(){
      return {
        currentPage:'',
        numOfPage:'',
        columns:[],
        persons:{},
    }
  },
  created(){
      this.firstPageLoaded(currentPage)
  },
  methods:{
      getPersonData(currentPage){
        const config ={
            'content-type':'application/json',
            headers:{
            'Access-Control-Request-Headers': '',
            },
        }
        return axios.get('http://54.180.115.81:8000/polls/person/'+currentPage,config).then((response)=>{
            this.persons=response.data['persons']
            this.columns=response.data['columns']
            this.numOfPage=parseInt(response.data['count']/10)
        }).catch((e)=>{
            console.log(e);
        })
      },
      firstPageLoaded(currentPage){
          getPersonData(currentPage)
          currentPage=1

      }
  },
  components:{
      Pagination,
  }
}
</script>