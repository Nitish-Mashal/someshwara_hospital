<template>
  <div>
    <Navbar />
    <router-view />
    <FloatingEnquiry />
    <WhatsappFloat />
    <ScrollToTop /> 
    <Footer /> 
  </div>
</template>

<script setup>
import Navbar from './Navbar/Navbar.vue'
import Footer from './Footer/Footer.vue'
import ScrollToTop from './ScrollToTop.vue'
import WhatsappFloat from './WhatsappFloat.vue'
import FloatingEnquiry from './FloatingEnquiry.vue'

import { onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// setup router
const route = useRoute()
const router = useRouter()

// lifecycle
onMounted(() => {
  console.log('Component mounted')
})

// watch example (optional)
watch(
  () => route.path,
  (newPath, oldPath) => {
    console.log(`Route changed from ${oldPath} to ${newPath}`)
  }
)
</script>