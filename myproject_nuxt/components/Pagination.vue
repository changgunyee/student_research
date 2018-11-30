<template>
    <tr>
        <td v-for="page in numOfPage" :key="page.key">
            {{page}}
        </td>
    </tr>
</template>
<script>
export default{
    data(){
        return {
            count:0
        }
    },
    computed:{
        numOfPage(){
            return this.count/10+1
        },
    }
}
</script>