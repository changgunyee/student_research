<template>
    <tr>
        <td v-for="page in numOfPage" :key="page.key" @click="changePage($event)">
            {{page}}
        </td>
    </tr>
</template>
<script>
export default{
    props:['count'],
    data(){
        return {
            numOfPage:parseInt((this.count-1)/10)+1
        }
    },
    watch:{
        count(newVal){
            this.numOfPage=parseInt((this.count-1)/10)+1
        }
    },
    methods:{ 
        changePage(event){
          this.$emit("changePageInter",event.currentTarget.innerText)
        },
    }
}
</script>