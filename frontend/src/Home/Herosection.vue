<template>
    <div>

        <!-- Carousel Section -->
        <section class="w-full leading-none">

            <!-- 🔥 IMMEDIATE HERO IMAGE -->
            <div v-if="firstBanner && !carouselReady" class="w-full overflow-hidden relative">

                <component :is="firstBanner.link ? 'a' : 'div'" :href="firstBanner.link || undefined"
                    :target="firstBanner.external_site ? '_blank' : '_self'"
                    :rel="firstBanner.external_site ? 'noopener noreferrer' : undefined" class="block w-full h-full">

                    <!-- ✅ FIXED IMAGE -->
                    <img :src="resolveBannerImage(firstBanner)" :alt="getBannerAlt(firstBanner)" fetchpriority="high"
                        decoding="async" class="w-full h-auto sm:h-[400px] object-contain sm:object-cover block" />
                </component>
            </div>

            <!-- 🎠 CAROUSEL -->
            <el-carousel v-if="carouselReady" :interval="3000" :pause-on-hover="false" indicator-position="none"
                arrow="never" class="w-full banner-carousel">
                <el-carousel-item v-for="(banner, index) in banners" :key="index">
                    <component :is="banner.link ? 'a' : 'div'" :href="banner.link || undefined"
                        :target="banner.external_site ? '_blank' : '_self'"
                        :rel="banner.external_site ? 'noopener noreferrer' : undefined"
                        class="block w-full h-full relative">

                        <!-- ✅ FIXED IMAGE (MAIN FIX) -->
                        <img :src="resolveBannerImage(banner)" :alt="getBannerAlt(banner)"
                            class="w-full h-auto sm:h-full object-contain sm:object-cover block"
                            :loading="index === 0 ? 'eager' : 'lazy'" :fetchpriority="index === 0 ? 'high' : 'auto'"
                            decoding="async" />

                        <!-- 🔥 BUTTONS -->
                        <div class="absolute bottom-24 left-10 sm:left-20 lg:left-40 hidden sm:flex gap-3 z-50">
                            <router-link to="/doctors-list">
                                <button class="bg-blue-700 text-white px-4 py-2 rounded-lg font-semibold">
                                    Book Appointment
                                </button>
                            </router-link>

                            <a href="tel:+919945141393"
                                class="bg-yellow-400 px-4 py-2 rounded-lg font-semibold text-white flex items-center gap-2 no-underline">

                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor"
                                    viewBox="0 0 24 24">
                                    <path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24
                                    11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1
                                    A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1
                                    11.36 11.36 0 00.57 3.56 1 1 0 01-.24 1.01l-2.2 2.22z" />
                                </svg>

                                Call Us
                            </a>
                        </div>

                    </component>
                </el-carousel-item>
            </el-carousel>

        </section>

        <!-- ⬇️ Rest -->
        <Trustbar />
        <AboutSection />
        <OurServices />
        <Drprofile />
        <Utility />
        <Whychooseus />
        <Testimonials />

    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, defineAsyncComponent } from 'vue'

const Trustbar = defineAsyncComponent(() => import('./Trustbar.vue'))
const AboutSection = defineAsyncComponent(() => import('./AboutSection.vue'))
const OurServices = defineAsyncComponent(() => import('./OurServices.vue'))
const Drprofile = defineAsyncComponent(() => import('./Drprofile.vue'))
const Utility = defineAsyncComponent(() => import('./Utility.vue'))
const Whychooseus = defineAsyncComponent(() => import('./Whychooseus.vue'))
const Testimonials = defineAsyncComponent(() => import('./Testimonial.vue'))

const banners = ref([])
const firstBanner = ref(null)
const carouselReady = ref(false)

const isMobile = ref(window.innerWidth < 640)

function handleResize() {
    isMobile.value = window.innerWidth < 640
}

onMounted(() => {
    window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
})

function resolveBannerImage(banner) {
    if (!banner) return null

    return isMobile.value
        ? banner.upload_mobile_image || banner.upload_desktop_image
        : banner.upload_desktop_image || banner.upload_mobile_image
}

function getBannerAlt(banner) {
    if (!banner) return 'Someshwara Multispeciality Hospital'

    const title =
        banner.name1 ||
        banner.meta_title ||
        banner.title

    return title
        ? `Someshwara Multispeciality Hospital - ${title}`
        : 'Someshwara Multispeciality Hospital'
}

async function loadBanners() {
    try {
        const res = await fetch(
            '/api/method/someshwara_hospital.api.banner_image.get_banner_images'
        )
        const json = await res.json()

        firstBanner.value = json.message.first_banner
        banners.value = json.message.data || []

        if (!firstBanner.value) return

        const img = new Image()
        img.src = resolveBannerImage(firstBanner.value)

        if (img.complete) {
            carouselReady.value = true
        } else {
            img.onload = () => {
                carouselReady.value = true
            }
        }

    } catch (e) {
        console.error('Banner API error:', e)
    }
}

onMounted(loadBanners)
</script>

<style scoped>
/* 🔥 REMOVE ANY GAP */
.banner-carousel img {
    display: block;
}

/* 🔥 MOBILE = AUTO HEIGHT (NO GAP) */
.banner-carousel :deep(.el-carousel__container),
.banner-carousel :deep(.el-carousel__item),
.banner-carousel :deep(.el-carousel__item > div) {
    height: 120px;
}

/* 🔥 DESKTOP HEIGHT */
@media (min-width: 640px) {

    .banner-carousel :deep(.el-carousel__container),
    .banner-carousel :deep(.el-carousel__item),
    .banner-carousel :deep(.el-carousel__item > div) {
        height: 400px;
    }
}
</style>