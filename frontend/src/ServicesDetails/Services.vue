<template>
    <section class="">

        <!-- HEADER -->
        <!-- ================= BANNER ================= -->
        <div class="relative w-full mb-8 overflow-hidden">

            <img :src="getFileUrl('services-banner.jpg')" alt="services-banner"
                class="w-full h-[180px] sm:h-[240px] md:h-[380px] object-cover" />

            <!-- 🔵 THEME OVERLAY -->
            <div class="absolute inset-0 bg-blue-700/40"></div>
            <!-- TEXT -->
            <div class="absolute inset-0 flex items-center justify-center z-10 px-6">
                <h1 class="text-white font-semibold text-center text-2xl md:text-5xl">
                    Services
                </h1>
            </div>
        </div>

        <!-- CARDS -->
        <div class="container">
            <div class="row justify-content-center">

                <article v-for="service in services" :key="service.url" class="col-md-4 d-flex">
                    <div class="bg-white rounded-2xl w-full p-6 text-center mb-5 flex flex-col
                shadow-md transition duration-300
                hover:shadow-xl hover:-translate-y-2">

                        <!-- IMAGE -->
                        <div class="flex justify-center mb-4">
                            <div class="bg-blue-700/10 p-1 rounded-full">
                                <img :src="getImage(service.home_icon)" :alt="service.name1"
                                    class="w-20 h-20 object-contain" />
                            </div>
                        </div>

                        <!-- NAME -->
                        <h5 class="text-blue-700 font-semibold mb-3 text-lg">
                            {{ service.name1 }}
                        </h5>

                        <!-- DESCRIPTION -->
                        <p class="text-gray-600 text-sm flex-1">
                            {{ getShortText(service.description) }}
                        </p>

                        <!-- CTA -->
                        <div class="mt-4">
                            <router-link :to="{ name: 'ServiceDetails', params: { slug: service.url } }"
                                class="inline-block text-sm font-medium text-blue-700 hover:text-yellow-400 transition">
                                Learn More →
                            </router-link>
                        </div>

                    </div>
                </article>

            </div>
        </div>

    </section>
</template>

<script setup>
import { ref, onMounted } from "vue"

const services = ref([])

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

/* ---------------- FETCH SERVICES ---------------- */
const fetchServices = async () => {
    try {
        const res = await fetch(
            "/api/method/someshwara_hospital.api.our_services.get_our_services"
        )
        const data = await res.json()

        if (data.message?.status === "success") {
            services.value = data.message.data
        }
    } catch (err) {
        console.error("Error fetching services:", err)
    }
}

/* ---------------- IMAGE ---------------- */
const getImage = (img) => {

    // Placeholder image
    const placeholder = "/files/services-placeholder-icon.png"

    // If no image uploaded
    if (!img) return placeholder

    // If full URL
    if (img.startsWith("http")) {
        return img
    }

    // Relative backend image path
    return img || placeholder
}

/* ---------------- CLEAN DESCRIPTION ---------------- */
const getShortText = (html) => {
    if (!html) return ""

    const div = document.createElement("div")
    div.innerHTML = html

    return div.innerText.slice(0, 120) + "..."
}

/* ---------------- MOUNT ---------------- */
onMounted(fetchServices)
</script>