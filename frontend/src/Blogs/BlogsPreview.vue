<template>
    <div class="container py-10">

        <!-- Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">

            <div v-for="(card, index) in cards" :key="index"
                class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1 flex flex-col border-t-4 border-yellow-400">

                <!-- 🔷 TOP -->
                <div class="bg-blue-700 p-4 flex justify-between items-center h-48">

                    <!-- LEFT -->
                    <div class="text-white w-1/2">
                        <h2 class="text-lg font-bold leading-snug">
                            {{ card.description_heading_1 || 'Untitled' }}
                        </h2>
                        <h3 class="text-yellow-300 text-sm font-medium mt-1">
                            {{ card.sub_description_heading_1 || '' }}
                        </h3>
                    </div>

                    <!-- RIGHT IMAGE -->
                    <div class="w-1/2 flex justify-center">
                        <img :src="card.thumbnail_image" :alt="getBlogAlt(card)"
                            class="w-28 h-28 object-cover rounded-full border-4 border-yellow-400 shadow-md" />
                    </div>
                </div>

                <!-- 🔹 CONTENT -->
                <div class="p-4 flex-1">

                    <h3 class="text-lg font-semibold text-blue-700 mb-2">
                        {{ card.description_heading_2 || card.description_heading_1 }}
                    </h3>

                    <p class="text-gray-600 text-sm mb-3 line-clamp-3">
                        {{ stripHtml(card.description_1) }}
                    </p>

                    <router-link v-if="card.url" :to="{ name: 'BlogDetails', params: { slug: card.url } }"
                        class="inline-block text-blue-700 font-semibold text-sm hover:text-yellow-500 transition">
                        Read More →
                    </router-link>
                </div>

                <!-- 🔸 FOOTER -->
                <div class="border-t border-blue-100 px-4 py-2 bg-blue-50">
                    <div class="text-blue-700 text-xs font-medium">
                        {{ formatDate(card.blog_date) }}
                    </div>
                </div>

            </div>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const cards = ref([]);

/* ---------------- UTIL ---------------- */
const stripHtml = (html) => {
    if (!html) return "";
    const temp = document.createElement("div");
    temp.innerHTML = html;
    return temp.textContent || temp.innerText || "";
};

const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const date = new Date(dateStr);
    return date.toLocaleDateString("en-IN", {
        year: "numeric",
        month: "long",
        day: "numeric",
    });
};

const getBlogAlt = (card) => {
    if (!card?.description_heading_1) {
        return 'Someshwara Hospital';
    }
    return `Someshwara Hospital - ${card.description_heading_1}`;
};

const generateSlug = (text) =>
    text?.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');

/* ---------------- FETCH ---------------- */
onMounted(async () => {
    try {
        const res = await fetch("/api/method/someshwara_hospital.api.blogs.get_blogs");
        const data = await res.json();

        console.log("API RESPONSE:", data);

        // ✅ SAFE HANDLING
        const blogs = Array.isArray(data.message)
            ? data.message
            : Array.isArray(data.message?.data)
                ? data.message.data
                : [];

        cards.value = blogs.map(card => ({
            ...card,
            url: card.url || generateSlug(card.name)
        }));

    } catch (error) {
        console.error("❌ Error fetching blogs:", error);
    }
});
</script>