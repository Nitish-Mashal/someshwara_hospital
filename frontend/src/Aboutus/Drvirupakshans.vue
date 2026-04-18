<template>
    <section>

        <!-- 🔥 HERO BANNER -->
        <div class="relative w-full h-[240px] md:h-[420px] overflow-hidden">

            <img :src="getFileUrl('about-us-image.jpg')" alt="Dr Virupaksha N.S - Someshwara Hospital"
                class="w-full h-full object-cover" />

            <!-- WHITE OVERLAY -->
            <div class="absolute inset-0 bg-white/60"></div>

            <!-- TEXT -->
            <div class="absolute inset-0 flex flex-col items-center justify-center text-center px-4">
                <h1 class="text-3xl md:text-5xl font-bold text-blue-700 mb-2">
                    Dr. Virupaksha N. S.
                </h1>
                <p class="text-lg md:text-xl text-yellow-500 font-semibold">
                    Founder & Chief Consultant
                </p>
            </div>
        </div>

        <!-- 🔵 PROFILE SECTION -->
        <div class="max-w-6xl mx-auto px-5 py-10">

            <div class="grid md:grid-cols-2 gap-10 items-center">

                <!-- 👨‍⚕️ DOCTOR IMAGE -->
                <div class="flex justify-center">
                    <img :src="getFileUrl('dr-virupaksha-ns.jpg')" alt="Dr Virupaksha N.S"
                        class="w-full max-w-md rounded-2xl shadow-lg object-cover" />
                </div>

                <!-- 📝 INTRO -->
                <div>
                    <h2 class="text-2xl md:text-3xl font-semibold text-blue-700 mb-3">
                        Orthopedic Surgeon & Interventional Pain Specialist
                    </h2>

                    <p class="text-gray-700 mb-4 leading-relaxed">
                        Dr. Virupaksha N. S. is a highly experienced Orthopedic Surgeon with over
                        <strong>25+ years of clinical expertise</strong> in treating musculoskeletal
                        disorders and chronic pain through advanced surgical and non-surgical approaches.
                    </p>

                    <div class="bg-blue-700 text-white rounded-xl p-4 shadow-md">
                        <p class="text-sm">
                            ✔ Successfully treated <strong>10,000+ patients</strong> with conditions like
                            disc bulge, sciatica, arthritis, joint injuries, and sports-related disorders.
                        </p>
                    </div>
                </div>

            </div>

            <!-- SPECIALIZATION -->
            <div class="mt-10">
                <h3 class="text-xl font-semibold text-blue-700 mb-4 border-l-4 border-yellow-400 pl-3">
                    Areas of Specialization
                </h3>

                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    <div v-for="item in specializations" :key="item"
                        class="bg-blue-50 text-blue-700 px-4 py-3 rounded-lg text-sm font-medium shadow-sm">
                        {{ item }}
                    </div>
                </div>
            </div>

            <!-- HOLISTIC -->
            <div class="mt-10">
                <h3 class="text-xl font-semibold text-blue-700 mb-3 border-l-4 border-yellow-400 pl-3">
                    Holistic Approach
                </h3>

                <p class="text-gray-700 leading-relaxed">
                    Dr. Virupaksha believes in a holistic mind–body approach, integrating modern orthopedic
                    treatments with lifestyle medicine, exercise therapy, yoga, and pranayama to promote
                    long-term health and recovery.
                </p>
            </div>

            <!-- SERVICE -->
            <div class="mt-10">
                <h3 class="text-xl font-semibold text-blue-700 mb-3 border-l-4 border-yellow-400 pl-3">
                    Commitment to Service
                </h3>

                <ul class="list-disc pl-5 text-gray-700 space-y-2">
                    <li>Free treatment for Clubfoot children since 2014</li>
                    <li>Medical support during Coorg natural calamities</li>
                    <li>Strong focus on compassionate and accessible care</li>
                </ul>
            </div>

            <!-- WELLNESS -->
            <div class="mt-10">
                <h3 class="text-xl font-semibold text-blue-700 mb-3 border-l-4 border-yellow-400 pl-3">
                    Wellness & Lifestyle Care
                </h3>

                <p class="text-gray-700 leading-relaxed">
                    Focuses on metabolic health including Diabetes, Hypertension, PCOD/PCOS,
                    Thyroid disorders, Allergies, and Obesity through holistic transformation.
                </p>
            </div>

            <!-- CTA -->
            <div class="text-center mt-10">
                <router-link to="/appointment-page">
                    <button
                        class="bg-yellow-400 text-white px-6 py-3 rounded-lg font-semibold shadow-md hover:opacity-90 transition">
                        Book Appointment
                    </button>
                </router-link>
            </div>

        </div>

    </section>
</template>

<script setup>
const specializations = [
    "Orthopedic Surgery",
    "Trauma Care",
    "Arthroscopy",
    "Joint Replacement",
    "Sports Medicine",
    "Pediatric Orthopedics",
    "Interventional Pain Management"
]

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};
</script>