<template>
    <table class="table">
        <tr>
            <th>{{name}}</th>
            <td>{{email}}</td>
            <td v-for="answer in answers" v-bind:key="answer.id">{{answer}}</td>
        </tr>
    </table>
</template>
<script>
export default{
    props:['name','email',"answers"]
}
</script>

<style>
table{
    table-layout: fixed
}
</style>
