<template>
    <div class="flex w-full items-center">
      <div class="mx-auto w-1/2">
        <DataTable class="display" :columns="columns" :data="data.data" :options="options"/>
      </div>
    </div>
  </template>

<script setup>
import { useFetch } from '@/composable/useFetch.js'

import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-dt';
import { onMounted, ref } from 'vue';


DataTable.use(DataTablesCore);

const data = ref({})

const options = {
    responsive: true,
    select: true,
    paging: false,
    searching: false

}

const { tryFetching } = useFetch()

const columns = [
    { data: "username", title: 'Username' },
    { data: "count_tweet", title: 'Tweet Counts' },
];

onMounted(async () => {
    const res = await tryFetching('/api/counts')
    data.value = res.data
})

</script>

<style >
@import 'datatables.net-dt';
</style>
