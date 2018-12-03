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
            numOfPage:this.count
        }
    },
    computed:{
        numOfPage(){
            return parseInt(this.numOfPage/10)+1
        },
    },
    watch:{
        count(newVal){
            this.numOfPage=newVal
        }
    }
}
</script>