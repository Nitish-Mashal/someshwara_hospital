<template>
    <section class="mt-5 py-10 bg-blue-50">

        <!-- HEADER -->
        <div class="container position-relative text-center mb-8">

            <!-- CENTER CONTENT -->
            <div>
                <h3 class="text-3xl font-semibold text-blue-700">
                    Our Services
                </h3>

                <p class="text-gray-600 mt-2 max-w-2xl mx-auto">
                    Delivering expert care across multiple specialties with advanced technology and compassionate
                    treatment.
                </p>
            </div>

            <!-- VIEW ALL -->
            <router-link to="/services"
                class="position-absolute top-0 end-0 text-blue-700 font-medium text-decoration-none hover:text-yellow-400 transition">
                View All →
            </router-link>

        </div>

        <!-- CARDS -->
        <div class="container">
            <div class="row justify-content-center">

                <article v-for="service in services.slice(0, 5)" :key="service.url" class="col-md-4 d-flex">
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