<template>
    <label>{{ labelName }}</label>
    <input :type="inputType"  :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="rounded-md focus:bg-white focus:outline-none focus:border-b-4 focus:border-slate-700 h-10 w-50"/>
</template>

<script setup>
defineProps(['labelName', 'inputType', 'modelValue'])
defineEmits(['update:modelValue'])
</script>