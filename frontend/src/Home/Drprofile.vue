<template>
    <section class="container my-5">

        <article v-for="leader in leaders" :key="leader.name" class="row align-items-center gy-4">

            <!-- IMAGE -->
            <div class="col-md-5">
                <div class="relative">
                    <img :src="leader.image" :alt="leader.name" class="rounded-2xl shadow-lg w-full object-cover" />

                    <!-- Accent -->
                    <div class="absolute -bottom-4 -left-4 bg-yellow-400 w-20 h-20 rounded-xl hidden md:block"></div>
                </div>
            </div>

            <div class="col-md-1"></div>

            <!-- CONTENT -->
            <div class="col-md-6">

                <!-- LABEL -->
                <p class="text-yellow-400 uppercase mb-2 tracking-widest font-medium">
                    Leadership
                </p>

                <!-- TITLE -->
                <h2 class="text-3xl font-semibold mb-3 text-blue-700">
                    Our Visionary Leader
                </h2>

                <!-- NAME -->
                <h3 class="text-xl text-blue-700 font-semibold mb-1">
                    {{ leader.name }}
                </h3>

                <!-- QUALIFICATION -->
                <p class="font-medium mb-2 text-yellow-400">
                    {{ leader.qualifications }}
                </p>

                <!-- DESIGNATION -->
                <p class="mb-3 font-semibold text-gray-700">
                    {{ leader.designation }}
                </p>

                <!-- DESCRIPTION -->
                <p class="mb-4 text-gray-600 leading-relaxed">
                    {{ leader.description }}
                </p>

                <!-- CTA -->
                <a :href="leader.link" target="_blank" class="inline-block bg-blue-700 text-white px-6 py-2 rounded-xl font-semibold
                          hover:bg-yellow-400 hover:text-blue-700 transition duration-300">
                    View Profile →
                </a>

            </div>

        </article>

    </section>
</template>

<script setup>

/* Static → no ref needed */
const leaders = Object.freeze([
    {
        name: "Dr. Virupaksha N. S.",
        qualifications: "MBBS, MS (Orthopaedics)",
        designation: "Orthopaedic Surgeon & Trauma Specialist",
        description:
            "Dr. Virupaksha N. S. is a highly experienced orthopaedic surgeon specializing in trauma care, joint disorders, and fracture management. With a strong focus on patient-centered care, he is known for his precise diagnosis, advanced surgical skills, and compassionate approach. His expertise extends to treating complex orthopaedic conditions, helping patients regain mobility and lead pain-free lives through both surgical and non-surgical treatments.",
        image: "/files/dr-virupaksha-ns.jpg",
        link: "https://someshwarahospital.com/dr-virupaksha-n-s/"
    }
])

</script>