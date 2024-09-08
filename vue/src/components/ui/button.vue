<template>
    <button :type="buttonType" class="bg-slate-700 p-2 mt-3 rounded-md text-white hover:bg-gray-950" > {{ name }}</button>
</template>

<script setup>
defineProps({
    class:String,
    isClicked: Boolean,
    buttonType: String,
    name:{
        type:String,
        defaul: "Submit"
    }
})
</script>