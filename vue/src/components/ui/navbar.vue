<template>
  <div class="bg-slate-700 flex justify-around h-10 text-white">
    <h3 class="text-2xl font-bold">Simple Twitter</h3>
    <ul class="flex justify-evenly items-center">
          <li class="mr-4">
            <RouterLink to="/" active-class="border-b-2 border-white"
              class="hover:border-b-4 hover:border-white p-1">Home</RouterLink>
          </li>
          <li class="mr-4">
            <RouterLink to="/leaderboard" active-class="border-b-2 border-white"
              class="hover:border-b-4 hover:border-white p-1">Leaderboard</RouterLink>
          </li>
          <li class="mr-4">
            <RouterLink to="/login" active-class="border-b-2 border-white"
              class="hover:border-b-4 hover:border-white p-1">Login</RouterLink>
          </li>
          <li>
            <button @click="handleLogout" class="hover:border-b-2 border-white">Logout</button>
          </li>
    </ul>
  </div>
</template>

  
<script setup>
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../../service/auth';
import { useRouter } from 'vue-router'
import { useAuth } from '@/composable/auth.js'

import { ref } from 'vue'
import Swal from 'sweetalert2'

const router = useRouter()
const { removeToken, accessToken } = useAuthStore()
const { tryLogOut } = useAuth()

const success = ref(false)
const successMessage = ref(null)



const handleLogout = () => {
  Swal.fire({
    title: 'Logout',
    text: "Apakah anda yakin mau logout?",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Ya'
  }).then(async (result) => {
    if (result.isConfirmed) {
      const res = await tryLogOut(import.meta.env.VITE_FLASK_API_BASEURL + '/api/auth/logout', accessToken)
      success.value = res.data.success
      successMessage.value = res.data.message
      removeToken()
      router.push('/login')
      if (success.value) {
        Swal.fire(
          'Logout!',
          successMessage.value,
          'success'
        )
      }
    }
  })
}

</script>