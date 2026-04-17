<template>
    <div class="w-full bg-white">

        <!-- ================= BANNER ================= -->
        <div class="relative w-full mb-6 overflow-hidden">

            <img src="/files/gallery-image.jpg" alt="Someshwara Hospital Gallery"
                class="w-full h-48 sm:h-56 md:h-80 object-cover" />

            <!-- BLUE OVERLAY -->
            <div class="absolute inset-0 bg-blue-900/60"></div>

            <!-- TEXT -->
            <div class="absolute inset-0 flex items-center justify-center px-4">
                <div class="text-center">
                    <h1 class="font-bold text-2xl md:text-4xl text-white">
                        Gallery
                    </h1>
                    <p class="text-yellow-300 mt-2 text-sm md:text-base">
                        Moments of Care & Healing at Someshwara Hospital
                    </p>
                </div>
            </div>
        </div>

        <!-- ================= TAG BUTTONS ================= -->
        <div v-if="tags.length" class="flex justify-center flex-wrap gap-3 mb-8 px-4">

            <button v-for="tag in tags" :key="tag" @click="activeTag = tag"
                class="px-5 py-2 rounded-full text-sm font-semibold transition-all duration-300" :class="activeTag === tag
                    ? 'bg-blue-700 text-white shadow-lg scale-105'
                    : 'bg-yellow-400 text-blue-700 hover:bg-yellow-300 hover:scale-105'">
                {{ tag }}
            </button>
        </div>

        <!-- ================= LOADING ================= -->
        <div v-if="loading" class="flex justify-center items-center py-14">

            <div class="w-10 h-10 border-4 border-blue-700 border-t-transparent rounded-full animate-spin"></div>

            <span class="ml-3 text-blue-700 font-semibold">
                Loading images...
            </span>
        </div>

        <!-- ================= EMPTY ================= -->
        <div v-else-if="!images.length" class="text-center text-gray-500 py-14">
            No images available for this category
        </div>

        <!-- ================= GALLERY ================= -->
        <div v-else class="container">
            <div class="row">

                <div v-for="(img, index) in images" :key="index" class="col-12 col-sm-6 col-md-4 mb-4">
                    <div class="relative h-60 rounded-xl overflow-hidden shadow-md group">

                        <!-- 🔥 BLUR BACKGROUND (fills empty space) -->
                        <img :src="img"
                            class="absolute inset-0 w-full h-full object-cover blur-md scale-110 opacity-40" />

                        <!-- ✅ MAIN IMAGE (FULLY VISIBLE) -->
                        <img :src="img" alt="Someshwara Hospital Gallery Image"
                            class="relative w-full h-full object-contain transition-all duration-300 group-hover:scale-105"
                            loading="lazy" />

                    </div>
                </div>

            </div>
        </div>

    </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";

/* ---------------- STATE ---------------- */
const loading = ref(true);
const tags = ref([]);
const imagesByTag = ref({});
const activeTag = ref("");

/* ---------------- COMPUTED ---------------- */
const images = computed(() => {
    return imagesByTag.value[activeTag.value] || [];
});

/* ---------------- METHODS ---------------- */
const fetchGalleryImages = async () => {
    try {
        const startTime = Date.now();

        const res = await fetch(
            "/api/method/someshwara_hospital.api.gallery.get_gallery_images"
        );

        const data = await res.json();
        const message = data.message || {};

        tags.value = message.tags || [];
        imagesByTag.value = message.images_by_tag || {};

        activeTag.value = tags.value[0] || "";

        const elapsed = Date.now() - startTime;
        setTimeout(() => {
            loading.value = false;
        }, Math.max(800 - elapsed, 0));

    } catch (error) {
        console.error("Failed to load gallery images:", error);
        loading.value = false;
    }
};

/* ---------------- LIFECYCLE ---------------- */
onMounted(fetchGalleryImages);
</script>

<style scoped>
/* SMOOTH IMAGE HOVER */
img {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* CARD HOVER EFFECT */
.group:hover {
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
}
</style>