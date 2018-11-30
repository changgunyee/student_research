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
            count:this.count
        }
    },
    computed:{
        numOfPage(){
            return this.count/10+1
        },
    }
}
</script>