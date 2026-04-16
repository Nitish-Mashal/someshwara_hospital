<template>
    <button v-if="showButton" @click="scrollToTop"
        class="fixed bottom-20 sm:bottom-6 right-6 bg-blue-700 text-white p-2 rounded-full shadow-lg hover:bg-[#1b6aa9] transition-all duration-300">
        <!-- Up Arrow Icon -->
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
        </svg>
    </button>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const showButton = ref(false)

const handleScroll = () => {
    showButton.value = window.scrollY > 200 // show button after scrolling 200px
}

const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth',
    })
}

onMounted(() => {
    window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
})
</script>
