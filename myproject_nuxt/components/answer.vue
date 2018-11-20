<template>
    <table>
        <tr>
            <th>{{name}}</th>
            <th>{{email}}</th>
            <th v-for="answer in answers">{{answer}}</th>
        </tr>
    </table>
</template>
<script>
export default{
    props:['name','email',"answers"]
}
</script>