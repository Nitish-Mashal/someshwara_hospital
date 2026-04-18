<template>
    <section class="container py-10" aria-label="Patient Testimonials">

        <!-- HEADER -->
        <header class="relative text-center mb-8">
            <h3 class="text-3xl font-semibold text-blue-700">
                Testimonials
            </h3>

            <!-- VIEW ALL -->
            <div class="absolute right-0 top-1/2 -translate-y-1/2 text-sm">
                <a href="https://www.google.com/search?sca_esv=829b6725c1213f11&rlz=1C1CHBF_enIN1023IN1023&sxsrf=ANbL-n4h5XcSDQ4C9XDQy1c91VUvHuv9mw:1776160799847&si=AL3DRZEsmMGCryMMFSHJ3StBhOdZ2-6yYkXd_doETEE1OR-qOR0Dx7V7abHglCsaSz0-jtPTgObAMjlVajlWs-iWUZekbmDh9bMMQrf-kUwvUlwOfoHAwlD_lRrGBx7GpTRpOQuxR1rMlBQE3tSrASAm_tQ8Vpd3wAJFc8WlDodR6rki0PVeDcRa4rm7O4bzlVJWl9hIP3G_1acfsPjPZn3ppom8j7JPFdRtxNs70pW03SoP5M2BTceslrAfWfeenbFhRCHsRcrB4Luf1yHm0pG5-mY-94yEsg%3D%3D&q=Someshwara+Hospital+%7C+Accident+%26+Trauma+%7C+Orthopedic,+Arthritis+%26+Pain+Management+%7C+Diabetes+Management+%7C+Gauribidanur+Reviews&sa=X&ved=2ahUKEwiqw6fMiu2TAxXUT2wGHYlbGX8Q0bkNegQIJBAH&cshid=1776160878015507&biw=1366&bih=617&dpr=1"
                    target="_blank" class="text-blue-700 font-medium hover:text-yellow-400 transition">
                    View All →
                </a>
            </div>
        </header>

        <div class="flex flex-col md:flex-row gap-8 items-stretch justify-center">

            <!-- LEFT SUMMARY -->
            <aside class="w-full md:w-[260px] shrink-0 flex items-center justify-center">

                <div
                    class="bg-blue-700 text-white rounded-2xl p-6 text-center shadow-lg w-full h-full flex flex-col items-center justify-center">

                    <div class="text-2xl font-bold mb-2">
                        EXCELLENT
                    </div>

                    <div class="flex justify-center gap-1 text-yellow-400 text-lg mb-2">
                        <i class="bi bi-star-fill" v-for="i in 5" :key="i"></i>
                    </div>

                    <p class="text-sm mb-2">
                        Based on <strong>3185 reviews</strong>
                    </p>

                    <img :src="getFileUrl('Google.svg')" alt="Google Reviews" class="h-6 mt-2" />

                </div>

            </aside>

            <!-- CAROUSEL -->
            <div class="w-full md:w-[900px]">

                <Carousel :items-to-show="3" :breakpoints="carouselBreakpoints" :wrap-around="true" :autoplay="4500"
                    :pause-autoplay-on-hover="true" :mouse-drag="true" :gap="20" :auto-height="true">

                    <Slide v-for="item in testimonials" :key="item.name + item.time">

                        <article class="bg-white  p-5 rounded-xl
                                        h-full flex flex-col shadow-sm
                                        hover:shadow-lg transition duration-300">

                            <!-- USER -->
                            <div class="flex items-center gap-3 mb-3">
                                <div
                                    class="h-10 w-10 rounded-full bg-blue-700 text-white flex items-center justify-center font-bold">
                                    {{ item.initial }}
                                </div>

                                <div>
                                    <div class="font-semibold text-gray-800">
                                        {{ item.name }}
                                    </div>
                                    <div class="text-xs text-gray-500">
                                        {{ item.time }}
                                    </div>
                                </div>
                            </div>

                            <!-- STARS -->
                            <div class="text-yellow-400 flex gap-1 mb-2 text-sm">
                                <i class="bi bi-star-fill" v-for="i in 5" :key="i"></i>
                            </div>

                            <!-- REVIEW -->
                            <p class="text-gray-600 text-sm flex-1 leading-relaxed">
                                {{
                                    item.expanded
                                        ? item.review
                                        : item.review.slice(0, 100) + (item.review.length > 100 ? '...' : '')
                                }}
                            </p>

                            <!-- BUTTON -->
                            <button v-if="item.review.length > 100" @click="toggleExpand(item)"
                                class="text-sm text-blue-700 mt-2 text-left hover:text-yellow-400 transition font-medium">
                                {{ item.expanded ? 'Show less' : 'Read more' }}
                            </button>

                        </article>

                    </Slide>

                    <template #addons>
                        <Navigation />
                    </template>

                </Carousel>

            </div>
        </div>

    </section>
</template>

<script setup>
import { ref } from "vue"
import { Carousel, Slide, Navigation } from "vue3-carousel"
import "vue3-carousel/dist/carousel.css"

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

const testimonials = ref([
    {
        name: "Mohan Tiwari",
        initial: "M",
        time: "2 months ago",
        review: "My son had elbow fracture fracture 6 years back when he was in 3rd std , dr virupaksha performed surgery , now my son is 9 th standard, his elbow joint is perfectly alright. We visit this hospital regularly for every problem. Highly recommended.",
        expanded: false
    },
    {
        name: "Balu Krishna",
        initial: "B",
        time: "2 months ago",
        review: "Myself balakrishna 35y I had prolotherapy treatment at someshwara hospital 2years back with Dr virupaksha The doctor explained the procedure clearly and was very supportive throughout The treatment has helped me with shoulder pain I've had significant improvement I'm happy with the results",
        expanded: false
    },
    {
        name: "Hema",
        initial: "H",
        time: "2 months ago",
        review: "I was admitted in Someshwara hospital for knee plating surgery one year back.the rooms and overall facilities are very good,the Dr virupaksha were very good person,he is very calm,patiently answers my doubtful questions.overall experience are excellent ♥️♥️",
        expanded: false
    },
    {
        name: "Lakshmi Devi",
        initial: "L",
        time: "2 months ago",
        review: "My mother had left patella surgery at someshwara hospital about 3 years back. The doctor explained everything clearly and the recovery was smooth. Now she's walking comfortably without issues. Highly satisfied with the care and support.",
        expanded: false
    }
])

function toggleExpand(item) {
    item.expanded = !item.expanded
}

const carouselBreakpoints = {
    0: { itemsToShow: 1 },
    768: { itemsToShow: 2 },
    1024: { itemsToShow: 3 }
}
</script>