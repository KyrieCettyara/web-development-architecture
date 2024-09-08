<template>
  <div class="bg-white rounded-lg shadow-lg mb-5 mt-5 hover:scale-105">
    <div class="bg-gray-200 p-3 text-gray-600">
      <p>{{ user }}</p>
    </div>
    <div class="p-4">
      <img v-if="imgPath" :src="imgPath" :alt="imgName">
      <p class="text-gray-800 font-bold text-2xl ">
        {{ tweet }}
      </p>
    </div>
   
  </div>
</template>


<script setup>
defineProps(['user', 'tweet', 'imgPath', 'imgName', 'tweet_id'])
</script>