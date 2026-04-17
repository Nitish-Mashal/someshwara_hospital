<template>
    <header class="sticky top-0 z-50 w-full bg-white">
        <nav class="flex items-center justify-between px-6 md:px-20 relative">

            <!-- LOGO -->
            <router-link to="/" class="flex items-center">
                <img src="/files/logo.png" alt="Someshwara Hospital Logo"
                    class="hidden sm:block h-20" />
                <img src="/files/logo.png" alt="Someshwara Hospital Mobile Logo"
                    class="block sm:hidden h-12" />
            </router-link>

            <!-- RIGHT SIDE -->
            <div class="flex items-center gap-6">

                <!-- DESKTOP MENU -->
                <ul class="hidden md:flex items-center space-x-6 text-[15px] font-medium">

                    <li>
                        <router-link to="/" class="hover:text-blue-600 text-gray-800 no-underline">
                            Home
                        </router-link>
                    </li>

                    <!-- ABOUT -->
                    <li class="relative group">
                        <router-link to="/about-us" class="hover:text-blue-600 text-gray-800 no-underline">
                            <div class="flex items-center gap-1 cursor-pointer hover:text-blue-600 text-gray-800">
                                About Us
                                <svg class="w-3 h-3 mt-[1px]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M19 9l-7 7-7-7" />
                                </svg>
                            </div>
                        </router-link>

                        <ul class="absolute left-1/2 top-full -translate-x-1/2 mt-0 min-w-[280px]
                            bg-white rounded-xl shadow-xl hidden group-hover:flex flex-col
                            px-5 py-4 space-y-4 z-[9999]">
                            <li>
                                <router-link to="/dr-virupaksha-n-s"
                                    class="block text-[14px] font-medium text-gray-800 hover:text-blue-600 no-underline">
                                    Dr Virupaksha N.S
                                </router-link>
                            </li>
                        </ul>
                    </li>

                    <!-- SERVICES -->
                    <li class="relative group">
                        <div class="flex items-center gap-1 cursor-pointer hover:text-blue-600 text-gray-800">
                            Services
                            <svg class="w-3 h-3 mt-[1px]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M19 9l-7 7-7-7" />
                            </svg>
                        </div>

                        <ul class="absolute left-1/2 top-full -translate-x-1/2
                            bg-white rounded-xl shadow-xl hidden group-hover:block
                            px-6 py-4 z-[9999] columns-3 column-gap-10 min-w-[720px]">
                            <li v-for="service in services" :key="service.url" class="break-inside-avoid mb-3">
                                <router-link :to="`/services/${service.url}`"
                                    class="block text-[14px] font-medium text-gray-800 hover:text-blue-600 no-underline">
                                    {{ service.name1 }}
                                </router-link>
                                <hr class="mt-2">
                            </li>
                        </ul>
                    </li>

                    <li>
                        <router-link to="/doctors-list" class="hover:text-blue-600 text-gray-800 no-underline">
                            Doctors
                        </router-link>
                    </li>

                    <li>
                        <router-link to="/gallery" class="hover:text-blue-600 text-gray-800 no-underline">
                            Gallery
                        </router-link>
                    </li>

                    <li>
                        <router-link to="/blog" class="hover:text-blue-600 text-gray-800 no-underline">
                            Blog
                        </router-link>
                    </li>

                    <li>
                        <router-link to="/contact-us" class="hover:text-blue-600 text-gray-800 no-underline">
                            Contact Us
                        </router-link>
                    </li>
                </ul>

                <!-- DESKTOP RIGHT ITEMS -->
                <div class="hidden md:flex items-center space-x-4 mt-[-10px]">

                    <a href="#"
                        class="bg-yellow-400 px-4 py-2 rounded-lg text-sm font-semibold text-white no-underline">
                        Login
                    </a>
                </div>

                <!-- MOBILE TOGGLE -->
                <button @click="toggleMenu" class="md:hidden text-gray-800">
                    <svg v-if="!isMenuOpen" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                    <svg v-else class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

            </div>
        </nav>

        <!-- ================= MOBILE BUTTONS OUTSIDE MENU ================= -->
        <div class="md:hidden px-4 py-2 flex gap-3 items-center">
            <router-link to="/doctors-list" class="flex-1">
                <button class="w-full bg-blue-600 text-white py-2 rounded-lg text-sm font-semibold">
                    Book an Appointment
                </button>
            </router-link>

            <!-- PHONE NUMBER (replacing Login) -->
            <a href="tel:919945141393"
                class="flex-1 flex items-center justify-center gap-2 bg-yellow-400 text-white py-2 rounded-lg text-sm font-semibold no-underline">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24
        11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1
        A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1
        11.36 11.36 0 00.57 3.56 1 1 0 01-.24 1.01l-2.2 2.22z" />
                </svg>
                Call
            </a>
        </div>


        <!-- ================= MOBILE MENU ================= -->
        <div v-show="isMenuOpen" class="md:hidden bg-white px-3 pb-4 mobile-menu-wrapper relative z-[99999]">
            <ul class="flex flex-col space-y-3 text-[15px] font-medium text-gray-800">

                <li><router-link to="/" class="text-gray-800 no-underline">Home</router-link></li>
                <!-- MOBILE About Us -->
                <li>
                    <div class="flex w-full justify-between items-center">

                        <!-- TEXT (normal navigation) -->
                        <router-link to="/about-us" class="text-gray-800 no-underline">
                            About Us
                        </router-link>

                        <!-- ARROW (ONLY opens dropdown) -->
                        <svg @click.stop="activeMobileDropdown = 'more'" class="w-4 h-4 cursor-pointer" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>

                    </div>
                </li>

                <!-- MOBILE SERVICES -->
                <li>
                    <div class="flex w-full justify-between items-center">

                        <!-- TEXT (optional navigation or just label) -->
                        <span class="text-gray-800">
                            Services
                        </span>

                        <!-- ARROW -->
                        <svg @click.stop="activeMobileDropdown = 'services'" class="w-4 h-4 cursor-pointer" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>

                    </div>
                </li>

                <!-- MOBILE DOCTORS -->
                <li><router-link to="/doctors-list" class="text-gray-800 no-underline">Doctors</router-link></li>

                <li><router-link to="/gallery" class="text-gray-800 no-underline">Gallery</router-link></li>

                <li><router-link to="/blogs" class="text-gray-800 no-underline">Blogs</router-link></li>

                <li><router-link to="/contact-us" class="text-gray-800 no-underline">Contact Us</router-link></li>

                <li>
                    <a href="#" class="block w-full text-gray-800 no-underline">
                        Login
                    </a>
                </li>

            </ul>
        </div>
        <!-- ================= MOBILE DROPDOWN CARD (COMPACT) ================= -->
        <div v-if="activeMobileDropdown"
            class="fixed inset-0 z-[100000] md:hidden flex items-start justify-center pt-24">
            <!-- Backdrop -->
            <div class="absolute inset-0 bg-black/30" @click="activeMobileDropdown = null"></div>

            <!-- Card -->
            <div class="relative bg-white w-[90%] max-w-[420px]
           rounded-xl shadow-2xl
           max-h-[65vh]
           flex flex-col">
                <!-- Header -->
                <div class="flex items-center justify-between px-4 py-3 border-b">
                    <h3 class="font-semibold text-sm uppercase tracking-wide">
                        {{ mobileDropdownTitles[activeMobileDropdown] }}
                    </h3>
                    <button @click="activeMobileDropdown = null" class="text-lg leading-none">
                        ✕
                    </button>
                </div>

                <!-- Scrollable List -->
                <div class="flex-1 overflow-y-auto overscroll-contain px-4 py-2">
                    <!-- SERVICES -->
                    <ul v-if="activeMobileDropdown === 'services'" class="divide-y">
                        <li v-for="service in services" :key="service.url">
                            <router-link :to="`/services/${service.url}`"
                                class="block py-3 text-[14px] font-medium text-gray-800 no-underline"
                                @click="activeMobileDropdown = null">
                                {{ service.name1 }}
                            </router-link>
                        </li>
                    </ul>

                    <!-- MORE -->
                    <ul v-if="activeMobileDropdown === 'more'" class="divide-y">
                        <li>
                            <router-link to="/dr-virupaksha-n-s"
                                class="block py-3 text-[14px] font-medium text-gray-800 no-underline"
                                @click="activeMobileDropdown = null">
                                Dr Virupaksha N.S
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>


    </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from "vue"
import { useRouter } from "vue-router"

const activeMobileDropdown = ref(null)
const isMenuOpen = ref(false)
const mobileServices = ref(false)
const mobileFacilities = ref(false)
const mobileMore = ref(false)

const services = ref([])
const facilities = ref([])

// ========================= FETCH DATA =========================
const fetchServices = async () => {
    try {
        const res = await fetch("/api/method/someshwara_hospital.api.our_services.get_our_services")
        const data = await res.json()
        if (data.message?.status === "success") services.value = data.message.data
    } catch (err) {
        console.error(err)
    }
}

// ========================= TOGGLE FUNCTIONS =========================
const toggleMenu = (event) => {
    event.stopPropagation() // <--- stop event bubbling to document
    isMenuOpen.value = !isMenuOpen.value
}

const toggleServices = () => (mobileServices.value = !mobileServices.value)
const toggleFacilities = () => (mobileFacilities.value = !mobileFacilities.value)
const toggleMore = () => (mobileMore.value = !mobileMore.value)

// ========================= CLICK OUTSIDE =========================
const handleClickOutside = (event) => {
    const mobileMenu = document.querySelector(".mobile-menu-wrapper")
    if (mobileMenu && !mobileMenu.contains(event.target)) {
        isMenuOpen.value = false
        mobileServices.value = false
        mobileFacilities.value = false
        mobileMore.value = false
    }
}

const mobileDropdownTitles = {
    services: "Services",
    facilities: "Facilities",
    more: "About Us"
}

// ========================= ROUTER WATCH =========================
const router = useRouter()
watch(
    () => router.currentRoute.value.fullPath,
    () => {
        isMenuOpen.value = false
        mobileServices.value = false
        mobileFacilities.value = false
        mobileMore.value = false
    }
)

// ========================= ON MOUNT =========================
onMounted(() => {
    fetchServices()
    document.addEventListener("click", handleClickOutside)
})

onBeforeUnmount(() => {
    document.removeEventListener("click", handleClickOutside)
})
</script>
