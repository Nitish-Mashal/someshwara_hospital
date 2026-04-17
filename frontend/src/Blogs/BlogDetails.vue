<template>
    <div class="bg-white">

        <!-- 🔷 BANNER -->
        <div v-if="blog?.header_image" class="relative w-full">

            <img :src="blog.header_image" :alt="getBlogAlt(blog)" class="w-full h-56 sm:h-64 md:h-96 object-cover" />

            <!-- Overlay -->
            <div class="absolute inset-0 bg-blue-900/60"></div>

            <!-- Title -->
            <div class="absolute inset-0 flex items-center justify-center text-center px-4">
                <h1 class="text-white text-2xl md:text-4xl font-bold max-w-3xl">
                    {{ blog.description_heading_1 }}
                </h1>
            </div>
        </div>

        <!-- 🔹 CONTENT -->
        <div class="max-w-5xl mx-auto px-5 py-10">

            <!-- Loading -->
            <div v-if="isLoading" class="text-center py-20 text-blue-700">
                Loading blog details...
            </div>

            <!-- Blog Content -->
            <div v-else-if="blog">

                <div v-for="(heading, index) in descriptionHeadings" :key="index" class="mb-6">

                    <h2 v-if="heading"
                        class="text-xl md:text-2xl font-semibold text-blue-700 mb-2 border-l-4 border-yellow-400 pl-3">
                        {{ heading }}
                    </h2>

                    <p v-if="descriptions[index]" class="text-gray-700 text-base md:text-lg leading-relaxed"
                        v-html="descriptions[index]" />
                </div>

                <!-- Custom HTML -->
                <div v-if="blog.custom_html" class="mt-6" v-html="blog.custom_html"></div>

            </div>

            <!-- Fallback -->
            <div v-else class="text-center text-gray-500 py-20">
                Blog not found.
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const blog = ref(null)
const isLoading = ref(true)
const descriptionHeadings = ref([])
const descriptions = ref([])

/* ---------------- FETCH ---------------- */
const fetchBlogDetails = async () => {
    const blogSlug = route.params.slug

    if (!blogSlug) {
        isLoading.value = false
        return
    }

    try {
        const response = await fetch('/api/method/someshwara_hospital.api.blogs.get_blogs')
        const res = await response.json()

        console.log("BLOG DETAILS RESPONSE:", res)

        // ✅ CORRECT DATA EXTRACTION
        const allBlogs = Array.isArray(res.message?.data)
            ? res.message.data
            : [];

        console.log("ALL BLOGS:", allBlogs)
        console.log("SLUG:", blogSlug)

        blog.value = allBlogs.find(b => b.url === blogSlug) || null

        console.log("FOUND BLOG:", blog.value)

        if (blog.value) {
            updatePageSEO(blog.value)

            descriptionHeadings.value = []
            descriptions.value = []

            for (let i = 1; i <= 4; i++) {
                const heading = blog.value[`description_heading_${i}`]
                const desc = blog.value[`description_${i}`]

                if (heading || desc) {
                    descriptionHeadings.value.push(heading || '')
                    descriptions.value.push(desc || '')
                }
            }
        }

    } catch (err) {
        console.error('Error fetching blog details:', err)
        blog.value = null
    } finally {
        isLoading.value = false
    }
}

/* ---------------- ALT ---------------- */
const getBlogAlt = (blog) => {
    if (!blog) return 'Someshwara Hospital'

    const title =
        blog.meta_title ||
        blog.title ||
        blog.description_heading_1

    return title
        ? `Someshwara Hospital - ${title}`
        : 'Someshwara Hospital'
}

/* ---------------- SEO ---------------- */
const updateMeta = (key, content, attr = 'name') => {
    if (!content) return

    let meta = document.querySelector(`meta[${attr}='${key}']`)
    if (!meta) {
        meta = document.createElement('meta')
        meta.setAttribute(attr, key)
        document.head.appendChild(meta)
    }
    meta.setAttribute('content', content)
}

const updatePageSEO = (data) => {
    const title =
        data.meta_title ||
        data.title ||
        `${data.package_name || 'Health Services'} | Someshwara Hospital`

    document.title = title

    updateMeta('description', data.meta_description || data.short_description)
    updateMeta('keywords', data.meta_keyword)
}

/* ---------------- INIT ---------------- */
onMounted(fetchBlogDetails)
</script>