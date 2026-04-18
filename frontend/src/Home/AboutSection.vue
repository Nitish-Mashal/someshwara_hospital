<template>
    <section class="container py-10">

        <div class="row items-center">

            <!-- IMAGE COLUMN -->
            <div class="col-md-6 relative mb-6 md:mb-0">

                <!-- Image Wrapper -->
                <div class="relative">
                    <img :src="getFileUrl('someshwara-hospital-about.png')" alt="Someshwara Hospital"
                        class="w-full h-auto rounded-2xl shadow-lg" />

                    <!-- Accent Box -->
                    <div class="absolute -bottom-4 -right-4 bg-yellow-400 w-24 h-24 rounded-xl hidden md:block"></div>
                </div>

            </div>

            <!-- TEXT COLUMN -->
            <div ref="textBlock" class="col-md-6 flex flex-col justify-center">

                <h2 class="text-3xl font-semibold text-blue-700 mb-4">
                    Someshwara Hospital
                </h2>

                <!-- Highlight Line -->
                <div class="w-16 h-1 bg-yellow-400 mb-4 rounded"></div>

                <p class="text-gray-600 mb-3 leading-relaxed">
                    Our hospital provides <strong class="text-blue-700">comprehensive medical services</strong>,
                    ranging from outpatient consultations and emergency care to specialised treatments and advanced
                    regenerative therapies.
                </p>

                <p class="text-gray-600 mb-3 leading-relaxed">
                    With a team of experienced doctors and skilled healthcare professionals, we ensure
                    <strong class="text-blue-700">accurate diagnosis, personalised treatment plans, and compassionate
                        care</strong>
                    throughout your recovery journey.
                </p>

                <p class="text-gray-600 mb-2 leading-relaxed">
                    We specialize in <strong class="text-blue-700">advanced orthopedic care</strong> and offer
                    innovative
                    treatments like
                    <strong class="text-yellow-400">Ozone Therapy & PRP Therapy</strong> to promote natural healing and
                    reduce pain.
                </p>

                <!-- CTA BUTTON -->
                <router-link to="/appointment-page">
                    <button class="bg-blue-700 text-white px-6 py-2 rounded-xl font-semibold
                                   hover:bg-yellow-400 hover:text-blue-700 transition duration-300 w-fit">
                        Book Appointment →
                    </button>
                </router-link>

            </div>

        </div>

    </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const textBlock = ref(null)

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

/* Optional: Counter logic (kept if you want to use later) */
const years = ref(0)
const clients = ref(0)

const animateCounter = (refValue, target, duration = 1500) => {
    let start = 0
    const stepTime = Math.max(16, duration / target)

    const timer = setInterval(() => {
        start++
        refValue.value = start
        if (start >= target) clearInterval(timer)
    }, stepTime)
}

onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            animateCounter(years, 15)
            animateCounter(clients, 15000)
            observer.disconnect()
        }
    }, { threshold: 0.3 })

    if (textBlock.value) observer.observe(textBlock.value)
})
</script>