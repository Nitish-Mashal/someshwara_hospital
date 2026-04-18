<template>
    <div>

        <!-- 🔷 HERO -->
        <section class="relative w-full h-64 md:h-80">
            <img :src="getFileUrl('DoctorsTeam.png')" class="w-full h-full object-cover" />

            <div class="absolute inset-0 bg-blue-900/60"></div>

            <div class="absolute inset-0 flex items-center justify-center">
                <h1 class="text-3xl md:text-5xl font-bold text-white">
                    Doctor Profile
                </h1>
            </div>
        </section>

        <!-- 🔹 CARD -->
        <div class="flex justify-center bg-gray-50 py-10 px-4">
            <div class="w-full max-w-5xl bg-white rounded-2xl shadow-lg overflow-hidden">

                <!-- Loading -->
                <div v-if="loading" class="p-10 text-center text-blue-700">
                    Loading doctor profile...
                </div>

                <!-- Error -->
                <div v-else-if="error" class="p-10 text-center text-red-500">
                    {{ error }}
                </div>

                <!-- PROFILE -->
                <div v-else-if="doctor">

                    <!-- TOP -->
                    <div class="flex flex-col md:flex-row items-center p-6 gap-6">

                        <img :src="doctor.image || '/files/PlaceholderImages.png'" :alt="doctorAltText"
                            class="w-44 h-52 object-cover rounded-xl shadow-md border-4 border-yellow-400" />


                        <!-- DETAILS -->
                        <div class="flex-1 text-center md:text-left">

                            <h2 class="text-3xl font-bold text-blue-700">
                                {{ doctor.first_name }}
                            </h2>

                            <p class="text-gray-600 font-medium mt-1">
                                {{ doctor.custom_qualification }}
                            </p>

                            <div class="w-16 h-1 bg-yellow-400 my-3 mx-auto md:mx-0 rounded"></div>

                            <p class="text-sm text-gray-600">
                                <span class="font-semibold text-blue-700">Hospital:</span>
                                {{ doctor.hospital || 'Not specified' }}
                            </p>

                        </div>
                    </div>

                    <!-- STATS -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 px-6 pb-6">

                        <div class="bg-blue-700 text-white text-center py-4 rounded-xl shadow">
                            <p class="text-sm">Experience</p>
                            <p class="font-semibold">
                                {{ doctor.custom_experience || 'N/A' }}
                            </p>
                        </div>

                        <div class="bg-yellow-400 text-blue-700 text-center py-4 rounded-xl shadow">
                            <p class="text-sm">Doctor ID</p>
                            <p class="font-semibold">
                                {{ doctor.name || 'N/A' }}
                            </p>
                        </div>

                        <div class="bg-blue-700 text-white text-center py-4 rounded-xl shadow">
                            <p class="text-sm">Department</p>
                            <p class="font-semibold">
                                {{ doctor.department || 'N/A' }}
                            </p>
                        </div>

                    </div>

                    <!-- CTA -->
                    <div class="px-6 pb-6">
                        <button @click="bookAppointment"
                            class="w-full bg-yellow-400 text-blue-700 font-semibold py-3 rounded-full hover:bg-yellow-300 transition">
                            Book Appointment
                        </button>
                    </div>

                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

// state
const doctor = ref(null);
const loading = ref(true);
const error = ref(null);

const route = useRoute();
const router = useRouter();

// ✅ helper function
const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

// computed
const doctorAltText = computed(() => {
    return doctor.value?.first_name
        ? `Someshwara Hospital - ${doctor.value.first_name}`
        : "Someshwara Hospital";
});

// fetch doctor
const fetchDoctor = async () => {
    loading.value = true;
    try {
        const doctorId = route.params.id;

        const res = await fetch(
            `/api/method/someshwara_hospital.api.doctor_list.get_doctor?id=${doctorId}`
        );

        if (!res.ok) throw new Error("Failed to fetch doctor");

        const data = await res.json();
        doctor.value = data.message || null;
    } catch (err) {
        console.error(err);
        error.value = "Unable to load doctor profile.";
    } finally {
        loading.value = false;
    }
};

// CTA
const bookAppointment = () => {
    if (!doctor.value) return;

    router.push({
        name: "AppointmentPage",
        query: {
            department: doctor.value.department,
            doctor_id: doctor.value.name,
            doctor_name: `${doctor.value.first_name || ""} ${doctor.value.last_name || ""}`.trim(),
        },
    });
};

// lifecycle
onMounted(fetchDoctor);
</script>