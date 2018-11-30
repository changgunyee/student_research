<template>
    <tr>
        <td v-for="page in numOfPage()" :key="page.key">
            {{page}}
        </td>
    </tr>
</template>
<script>
export default{
    props:['count_data'],
    data(){
        return {
            count:this.count_data
        }
    },
    computed:{
        numOfPage(){
            return this.count/10+1
        },
    }
}
</script>