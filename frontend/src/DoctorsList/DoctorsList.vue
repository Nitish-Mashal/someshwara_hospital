<template>
  <div>

    <!-- 🔷 HERO -->
    <section class="relative w-full">
      <img
        src="/files/DoctorsTeam.png"
        alt="Doctors"
        class="w-full h-48 sm:h-56 md:h-72 object-cover"
      />

      <!-- BLUE OVERLAY -->
      <div class="absolute inset-0 bg-blue-900/70"></div>

      <!-- TITLE -->
      <div class="absolute inset-0 flex items-center justify-center z-10">
        <h1 class="font-bold text-white text-2xl md:text-4xl tracking-wide">
          Our Doctors
        </h1>
      </div>
    </section>

    <!-- 🔹 DOCTORS GRID -->
    <section class="py-10 px-4 max-w-6xl mx-auto">

      <!-- Loading -->
      <div v-if="loading" class="text-center py-10 text-blue-700 font-medium">
        Loading doctors...
      </div>

      <!-- Error -->
      <div v-else-if="error" class="text-center py-10 text-red-500">
        {{ error }}
      </div>

      <!-- Doctors -->
      <div
        v-else-if="doctors.length"
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
      >
        <div
          v-for="doctor in doctors"
          :key="doctor.name"
          class="bg-white rounded-xl shadow-md overflow-hidden 
                 hover:shadow-xl transition-all duration-300 
                 hover:-translate-y-1 border-t-4 border-yellow-400"
        >

          <!-- IMAGE -->
          <div class="relative">
            <img
              :src="getImage(doctor.image)"
              :alt="doctor.first_name"
              class="w-full h-72 object-cover"
              loading="lazy"
            />
          </div>

          <!-- INFO -->
          <div class="text-center py-3 px-2">
            <h4 class="text-blue-700 font-semibold text-lg">
              {{ doctor.first_name }}
            </h4>
          </div>

          <!-- ACTION BUTTONS -->
          <div class="grid grid-cols-2">

            <!-- View Profile -->
            <router-link
              :to="{ name: 'ViewProfile', params: { id: doctor.name } }"
              class="text-center bg-blue-700 text-white py-2 font-medium 
                     hover:bg-blue-800 transition border-r border-blue-600"
            >
              View Profile
            </router-link>

            <!-- Book Now -->
            <button
              @click="bookAppointment(doctor)"
              class="bg-yellow-400 text-blue-900 py-2 font-semibold 
                     hover:bg-yellow-500 transition w-full"
            >
              Book Now
            </button>

          </div>
        </div>
      </div>

      <!-- Empty -->
      <div v-else class="text-center py-10 text-gray-400">
        No doctors available.
      </div>

    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const doctors = ref([]);
const loading = ref(true);
const error = ref(null);

const router = useRouter();

// ✅ Fetch Doctors
const fetchDoctors = async () => {
  try {
    const res = await fetch(
      "/api/method/someshwara_hospital.api.doctor_list.get_doctors"
    );

    const data = await res.json();

    doctors.value = (data.message || []).map((doc) => ({
      name: doc.name,
      first_name: doc.first_name,
      image: doc.image,
    }));
  } catch (err) {
    console.error(err);
    error.value = "Failed to load doctors.";
  } finally {
    loading.value = false;
  }
};

// ✅ Image Fix
const getImage = (path) => {
  if (!path) return "/files/PlaceholderImages.png";
  return path.startsWith("http")
    ? path
    : `${window.location.origin}${path}`;
};

// ✅ Book Appointment
const bookAppointment = (doctor) => {
  router.push({
    path: "/appointment",
    query: {
      doctor_id: doctor.name,
    },
  });
};

onMounted(fetchDoctors);
</script>

<style scoped>
/* Optional: Smooth hover feel */
button,
a {
  transition: all 0.25s ease;
}
</style>