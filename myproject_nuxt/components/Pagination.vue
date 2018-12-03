<template>
    <tr>
        <td v-for="page in numOfPage" :key="page.key" >@click="changePage($event)" @changePageInter="changePage2">
            {{page}}
        </td>
    </tr>
</template>
<script>
export default{
    props:['count'],
    data(){
        return {
            numOfPage:this.count
        }
    },
    watch:{
        count(newVal){
            this.numOfPage=newVal
        }
    },
    methods:{ 
        
    }
}
</script>