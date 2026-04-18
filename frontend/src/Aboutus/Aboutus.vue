<template>
    <section>

        <!-- 🔥 FULL WIDTH BANNER -->
        <div class="relative w-full h-[220px] md:h-[420px] overflow-hidden">

            <img :src="getFileUrl('about-us-image.jpg')" alt="Someshwara Hospital" class="w-full h-full object-cover" />

            <!-- WHITE OVERLAY -->
            <div class="absolute inset-0 bg-white/50"></div>

            <!-- TEXT OVERLAY -->
            <div class="absolute inset-0 flex flex-col items-center justify-center text-center px-4">
                <h1 class="text-3xl md:text-5xl font-bold text-blue-700 mb-2">
                    About Us
                </h1>
                <p class="text-gray-700 max-w-xl">
                    Delivering trusted, advanced, and compassionate healthcare for a healthier tomorrow.
                </p>
            </div>

        </div>

        <!-- 🔥 EXTENDED ABOUT SECTION -->
        <div class="container py-4">

            <div class="grid md:grid-cols-2 gap-8 items-center">

                <!-- Image Wrapper -->
                <div class="relative">
                    <img :src="getFileUrl('someshwara-hospital-about.png')" alt="Someshwara Hospital"
                        class="w-full h-auto rounded-2xl shadow-lg" />

                    <!-- Accent Box -->
                    <div class="absolute -bottom-4 -right-4 bg-yellow-400 w-24 h-24 rounded-xl hidden md:block"></div>
                </div>

                <!-- CONTENT -->
                <div>
                    <h3 class="text-2xl font-semibold text-blue-700 mb-3">
                        Excellence in Orthopedic & Pain Care
                    </h3>

                    <div class="w-14 h-1 bg-yellow-400 mb-4 rounded"></div>

                    <p class="text-gray-600 mb-3 leading-relaxed">
                        Someshwara Hospital is known for its excellence in orthopedic and pain management treatments.
                        We provide specialized care for joint disorders, spine conditions, fractures, and sports
                        injuries.
                    </p>

                    <p class="text-gray-600 mb-3 leading-relaxed">
                        Our hospital also focuses on advanced regenerative therapies such as PRP and Ozone Therapy,
                        which help promote natural healing and reduce the need for invasive procedures.
                    </p>

                    <p class="text-gray-600 mb-4 leading-relaxed">
                        With a patient-first approach, we ensure comfort, transparency, and continuous support
                        throughout your treatment journey.
                    </p>

                    <!-- CTA -->
                    <router-link to="/appointment-page">
                        <button class="bg-blue-700 text-white px-6 py-3 rounded-xl font-semibold
                                       hover:bg-yellow-400 hover:text-blue-700 transition">
                            Book Appointment →
                        </button>
                    </router-link>

                </div>

            </div>

        </div>

        <!-- 🔵 ABOUT CONTENT -->
        <div class="container pt-3">

            <div class="max-w-4xl mx-auto text-center">

                <h2 class="text-2xl md:text-3xl font-semibold text-blue-700 mb-4">
                    Someshwara Multispeciality Hospital
                </h2>

                <div class="w-16 h-1 bg-yellow-400 mx-auto mb-4 rounded"></div>

                <p class="text-gray-600 leading-relaxed mb-4">
                    Someshwara Hospital is a trusted healthcare center dedicated to providing high-quality,
                    patient-centered medical services. We specialize in orthopedic care, trauma management,
                    and advanced regenerative treatments designed to restore mobility and improve quality of life.
                </p>

                <p class="text-gray-600 leading-relaxed">
                    With a team of experienced doctors and modern medical infrastructure, we focus on accurate
                    diagnosis,
                    effective treatments, and compassionate care. Our goal is to ensure every patient receives
                    personalized
                    attention and the best possible outcomes through both surgical and non-surgical approaches.
                </p>

            </div>

        </div>

        <Utility />

        <!-- 🟡 VISION / MISSION / PHILOSOPHY -->
        <div class="bg-blue-700 py-10">

            <div class="container">

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

                    <!-- VISION -->
                    <div class="bg-white rounded-xl p-6 shadow-md text-center hover:shadow-lg transition">
                        <h3 class="text-blue-700 font-semibold text-xl mb-3">
                            Our Vision
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed">
                            To be a trusted healthcare center delivering advanced orthopedic and regenerative treatments
                            that improve lives and promote long-term wellness.
                        </p>
                    </div>

                    <!-- MISSION -->
                    <div class="bg-yellow-400 rounded-xl p-6 shadow-md text-center hover:shadow-lg transition">
                        <h3 class="text-blue-700 font-semibold text-xl mb-3">
                            Our Mission
                        </h3>
                        <p class="text-gray-800 text-sm leading-relaxed">
                            To provide ethical, evidence-based medical care with modern technology, accurate diagnosis,
                            and personalized treatments for every patient.
                        </p>
                    </div>

                    <!-- PHILOSOPHY -->
                    <div class="bg-white rounded-xl p-6 shadow-md text-center hover:shadow-lg transition">
                        <h3 class="text-blue-700 font-semibold text-xl mb-3">
                            Our Philosophy
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed">
                            We believe in compassion, integrity, patient-centered care, and continuous innovation to
                            deliver safe, effective, and high-quality healthcare.
                        </p>
                    </div>

                </div>

            </div>

        </div>

        <OurTeam />

    </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, defineAsyncComponent } from 'vue'

const Utility = defineAsyncComponent(() => import('../Home/Utility.vue'))
const OurTeam = defineAsyncComponent(() => import('./OurTeam.vue'))

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

</script>