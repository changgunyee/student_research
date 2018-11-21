<template>
    <tr>
        <th>{{name}}</th>
        <td>{{email}}</td>
        <td v-for="answer in answers" v-bind:key="answer.id">{{answer}}</td>
    </tr>
</template>
<script>
export default{
    props:['name','email',"answers"]
}
</script>

