<template>
    <section class="py-14 bg-[#f5f9ff]">

        <div class="container">

            <!-- CONTENT SECTION -->
            <div class="row items-center justify-center">

                <!-- Left CONTENT -->
                <div class="col-lg-6 flex items-center">

                    <div class="w-full">

                        <!-- Heading -->
                        <h2 class="text-3xl lg:text-4xl font-bold text-blue-700 mb-3 text-center lg:text-left">

                            Why Choose Someshwara Hospital?

                        </h2>

                        <!-- Accent Line -->
                        <div class="w-20 h-1.5 bg-yellow-400 rounded-full mb-4 mx-auto lg:mx-0">
                        </div>

                        <!-- Features -->
                        <ul class="space-y-8">

                            <li v-for="item in reasons" :key="item.text" class="flex items-center gap-5">

                                <!-- Icon -->
                                <div
                                    class="min-w-[56px] w-[56px] h-[56px] rounded-2xl bg-[#e8f1fb] flex items-center justify-center shadow-sm flex-shrink-0 border border-[#d9e8f7]">

                                    <svg class="w-6 h-6 text-blue-700" fill="none" stroke="currentColor"
                                        stroke-width="2" viewBox="0 0 24 24">

                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />

                                    </svg>

                                </div>

                                <!-- Text -->
                                <p class="text-gray-600 leading-snug mb-0">

                                    {{ item.text }}

                                </p>

                            </li>

                        </ul>

                    </div>

                </div>

                <!-- VIDEO SECTION -->
                <div class="col-lg-6 flex justify-center mb-10 lg:mb-0">

                    <div
                        class="relative w-full max-w-2xl aspect-video rounded-3xl overflow-hidden shadow-xl border border-[#d9e8f7] bg-white">

                        <!-- Thumbnail Placeholder -->
                        <button v-if="!videoLoaded" @click="loadVideo"
                            class="relative w-full h-full group flex items-center justify-center"
                            aria-label="Play explanation video">

                            <!-- Thumbnail -->
                            <img :src="thumbnailUrl"
                                alt="Someshwara Hospital - Watch how our advanced treatments help patients recover"
                                width="1280" height="720" loading="lazy" decoding="async"
                                class="w-full h-full object-cover" />

                            <!-- Overlay -->
                            <div
                                class="absolute inset-0 bg-gradient-to-t from-black/60 to-black/10 group-hover:from-black/70 transition duration-300">
                            </div>

                            <!-- Play Button -->
                            <div class="absolute inset-0 flex items-center justify-center">

                                <div
                                    class="w-20 h-20 rounded-full bg-white/90 flex items-center justify-center shadow-2xl group-hover:scale-110 transition duration-300">

                                    <svg class="w-10 h-10 text-blue-700" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M8 5v14l11-7z" />

                                    </svg>

                                </div>

                            </div>

                        </button>

                        <!-- Lazy iframe -->
                        <iframe v-else class="absolute inset-0 w-full h-full" :src="videoUrl"
                            title="Someshwara Hospital treatment explanation video" loading="lazy"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowfullscreen>
                        </iframe>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
import { ref } from 'vue'

/* Video State */
const videoLoaded = ref(false)

/* YouTube Video */
const videoId = 'YCdAn8ByJWU'
const videoUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`
const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`

function loadVideo() {
    videoLoaded.value = true
}

/* Features */
const reasons = Object.freeze([
    {
        text: 'Expert Orthopedic & Spine Care for Lasting Relief',
        alt: 'Someshwara Hospital - Advanced care for bones, joints & spine health'
    },
    {
        text: 'Treating the Root Cause, Not Just the Symptoms',
        alt: 'Someshwara Hospital - Personalized treatments focused on healing and recovery'
    },
    {
        text: 'Advanced Non-Surgical Solutions for Pain-Free Living',
        alt: 'Someshwara Hospital - Non-surgical therapies for pain and mobility improvement'
    },
    {
        text: 'Faster Recovery with Minimal Disruption to Daily Life',
        alt: 'Someshwara Hospital - Comprehensive pain management with faster recovery support'
    },
    {
        text: 'Promoting Natural Healing Through Regenerative Care',
        alt: 'Someshwara Hospital - Regenerative and ozone therapies for natural healing'
    },
])
</script>