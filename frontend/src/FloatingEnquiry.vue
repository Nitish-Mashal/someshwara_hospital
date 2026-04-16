<template>
    <div class="hidden md:block fixed top-1/2 -translate-y-1/2 right-[-85px]
               rotate-[-90deg]
               bg-yellow-400 text-white
               px-4 py-2
               font-semibold uppercase text-sm
               cursor-pointer
               shadow-lg
               rounded-t-md
               z-[99999]" @click="openEnquiry">
        Contact Us For Booking
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const openEnquiry = () => {
    router.push('/contact-us')
}
</script>
