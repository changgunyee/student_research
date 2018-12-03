<template>
    <tr>
        <td v-for="page in numOfPage" :key="page.key">
            {{page}}
        </td>
    </tr>
</template>
<script>
export default{
    props:['count'],
    data(){
        return {
            numOfPage:parseInt(this.count/10)+1
        }
    },
//    computed:{
//        numOfPage(){
//            return parseInt(this.numOfPage/10)+1
//        },
 //   },
    watch:{
        count(newVal){
            numOfPage=parseInt(this.count/10)+1
        }
    }
}
</script>