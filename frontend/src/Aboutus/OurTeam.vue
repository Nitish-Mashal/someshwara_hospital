<template>
    <div class="w-full bg-gradient-to-b from-blue-50 to-white py-12 px-4">

        <!-- ================= Leadership ================= -->
        <section class="max-w-6xl mx-auto text-center mb-16">
            <h1 class="text-3xl md:text-4xl font-bold text-blue-700">
                Our Team
            </h1>

            <div class="flex justify-center mt-3 mb-10">
                <div class="w-24 h-[4px] bg-yellow-400 rounded-full"></div>
            </div>

            <!-- Leader Card -->
            <div class="flex justify-center">
                <div
                    class="group bg-white/90 backdrop-blur-md shadow-xl rounded-3xl p-8 max-w-xl w-full relative overflow-hidden border border-blue-100 hover:shadow-2xl transition duration-300">

                    <!-- Glow -->
                    <div
                        class="absolute inset-0 bg-gradient-to-br from-blue-100/30 to-yellow-100/20 opacity-0 group-hover:opacity-100 transition duration-300">
                    </div>

                    <!-- Avatar -->
                    <div
                        class="relative w-28 h-28 mx-auto rounded-full overflow-hidden border-4 border-yellow-400 shadow-md">

                        <img v-if="leader.image && !leader.error" :src="leader.image" :alt="leader.name"
                            class="w-full h-full object-cover" @error="leader.error = true" />

                        <div v-else
                            class="w-full h-full bg-blue-700 text-white flex items-center justify-center text-3xl font-bold">
                            {{ leader.name.charAt(0) }}
                        </div>
                    </div>

                    <!-- Name -->
                    <h2 class="text-2xl font-bold text-blue-700 mt-4">
                        {{ leader.name }}
                    </h2>

                    <!-- Role Badge -->
                    <span
                        class="inline-block mt-2 px-4 py-1 bg-yellow-400 text-blue-800 text-sm font-semibold rounded-full shadow">
                        {{ leader.role }}
                    </span>

                    <!-- Description -->
                    <p class="text-gray-600 mt-4 leading-relaxed text-sm md:text-base">
                        {{ leader.description }}
                    </p>

                </div>
            </div>
        </section>

        <!-- ================= TEAM ================= -->
        <section class="max-w-6xl mx-auto text-center">
            <h1 class="text-3xl md:text-4xl font-bold text-blue-700">
                Administration & Departments
            </h1>

            <div class="flex justify-center mt-3 mb-12">
                <div class="w-24 h-[4px] bg-yellow-400 rounded-full"></div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">

                <div v-for="(person, index) in team" :key="index"
                    class="group relative bg-white rounded-2xl shadow-md p-6 text-center transition duration-300 hover:shadow-2xl hover:-translate-y-2 border border-gray-100 overflow-hidden">

                    <!-- Hover Glow -->
                    <div
                        class="absolute inset-0 bg-gradient-to-br from-blue-50 to-yellow-50 opacity-0 group-hover:opacity-100 transition duration-300">
                    </div>

                    <!-- Avatar -->
                    <div
                        class="relative w-20 h-20 mx-auto rounded-full overflow-hidden border-4 border-blue-700 shadow">

                        <img v-if="person.image" :src="person.image" :alt="person.name"
                            class="w-full h-full object-cover" />

                        <div v-else
                            class="w-full h-full bg-blue-700 text-white flex items-center justify-center text-xl font-bold">
                            {{ person.name.charAt(0) }}
                        </div>
                    </div>

                    <!-- Name -->
                    <h3 class="text-lg font-semibold text-blue-700 mt-4">
                        {{ person.name }}
                    </h3>

                    <!-- Role -->
                    <span
                        class="inline-block mt-1 px-3 py-1 bg-yellow-400 text-blue-800 text-xs font-semibold rounded-full">
                        {{ person.role }}
                    </span>

                    <!-- Description -->
                    <p class="text-gray-600 text-sm mt-4 leading-relaxed">
                        {{ person.description }}
                    </p>

                    <!-- Bottom Accent Line -->
                    <div
                        class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-blue-700 to-yellow-400 opacity-80">
                    </div>

                </div>

            </div>
        </section>

    </div>
</template>

<script setup>
const leader = {
    name: "Dr. Virupaksha N.S.",
    role: "Founder & Chief Doctor",
    image: "/files/dr-virupaksha-ns.jpg",
    description:
        "Leads Someshwara Hospital with precision care and an integrated approach. Focuses on personalized, root-cause-based treatment combining modern and holistic medicine.",
    error: false
}

const team = [
    {
        name: "Mr. Basavaraj",
        role: "Administrative Officer",
        image: "/files/Basavaraj.jpg",
        description: "Manages hospital operations as Incharge and Administrative Officer."
    },
    {
        name: "Bharathi",
        role: "OT & X-Ray Operations",
        image: "",
        description: "Oversees OT and X-Ray operations with a focus on efficiency, safety, and quality care."
    },
    {
        name: "Devika",
        role: "Nursing Head",
        image: "/files/Devika.jpg",
        description: "Oversees nursing services ensuring high standards of care and patient support."
    },
    {
        name: "Jayanthi",
        role: "Lab Incharge",
        image: "/files/Jayanthi.jpg",
        description: "Manages laboratory testing with precision and ensures reliable diagnostic results."
    },
    {
        name: "Manju",
        role: "Physiotherapist",
        image: "/files/Manju.jpg",
        description: "Helps patients regain mobility and recover through physiotherapy."
    },
    {
        name: "Nikhil",
        role: "OT Assistant",
        image: "/files/Nikhil.jpg",
        description: "Supports surgical procedures ensuring smooth and safe OT operations."
    },
    {
        name: "Rudresh",
        role: "Pharmacist",
        image: "",
        description: "Manages pharmacy services ensuring safe and effective medication use."
    },
    {
        name: "Nayaj",
        role: "Staff Nurse",
        image: "/files/Nayaj.jpg",
        description: "Provides attentive nursing care focusing on patient comfort and safety."
    },
    {
        name: "Pavitra",
        role: "OPD Manager",
        image: "/files/Pavitra.jpg",
        description: "Ensures smooth and patient-friendly outpatient services."
    },
    {
        name: "Tarun",
        role: "Night Duty Incharge",
        image: "",
        description: "Oversees night operations and ensures timely emergency care."
    }
]
</script>