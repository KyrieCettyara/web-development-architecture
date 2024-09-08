<template>
    <label :for="id" class="text-2md font-semibold">{{ label }}</label>
    <textarea :id="id" class="rounded-md bg-white focus:bg-white focus:outline-none focus:border-b-4 focus:border-slate-700 m-5 ..." placeholder="What?" :rows="row" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"></textarea>
</template>

<script setup>
defineProps(['label', 'id', 'modelValue', 'row'])
defineEmits(['update:modelValue'])
</script>