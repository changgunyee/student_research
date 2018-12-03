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
        <Pagination :count="count" @changePageInter="changePage"></Pagination>
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
      this.getPersonData(1)
  },
  methods:{
      getPersonData(currentPage){
        const config ={
            'content-type':'application/json',
            headers:{
            'Access-Control-Request-Headers': '',
            },
        }
        return axios.get('http://54.180.115.81:8000/polls/person/page/'+currentPage,config).then((response)=>{
            this.persons=response.data['persons']
            this.columns=response.data['columns']
            this.count=response.data['count']
            this.currentPage=1
        }).catch((e)=>{
            console.log(e);
        })
      },
      changePage(currentPage){
            this.getPersonData(currentPage)
            this.currentPage=currentPage
      },
  },
  components:{
      Pagination,
  }
}
</script>