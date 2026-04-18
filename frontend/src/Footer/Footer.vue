<template>
    <footer class="text-gray-700 pb-24 md:pb-0">

        <!-- MAIN FOOTER -->
        <div class="bg-blue-700 text-white px-5 py-10">
            <div class="container">
                <div class="row g-4">

                    <!-- LOGO & SOCIAL -->
                    <div class="col-md-3">
                        <img :src="getFileUrl('logo.png')" alt="Someshwara Hospital" class="h-20 mb-4 object-contain" />

                        <p class="mb-4 text-sm leading-relaxed">
                            {{ tagline }}
                        </p>

                        <!-- Social Icons -->
                        <div class="flex gap-3">
                            <a v-for="social in socialIcons" :key="social.icon" :href="social.url" target="_blank"
                                class="w-8 h-8 flex items-center justify-center
                                    bg-yellow-400 text-blue-700 rounded-full
                                    hover:bg-white hover:text-blue-700 transition">

                                <i :class="`bi ${social.icon}`"></i>
                            </a>
                        </div>
                    </div>

                    <!-- QUICK LINKS -->
                    <div class="col-md-3">
                        <h5 class="mb-4 text-yellow-400 font-semibold ml-8">
                            Quick Links
                        </h5>

                        <ul class="space-y-2 text-sm">
                            <li v-for="link in quickLinks" :key="link.path">
                                <router-link :to="link.path" class="text-white no-underline">
                                    {{ link.name }}
                                </router-link>
                            </li>
                        </ul>
                    </div>

                    <!-- SERVICES -->
                    <div class="col-md-3">
                        <h5 class="mb-4 text-yellow-400 font-semibold ml-8">
                            Services
                        </h5>

                        <ul class="space-y-2 text-sm">
                            <li v-for="service in services" :key="service.service" class="text-white">
                                {{ service.service }}
                            </li>
                        </ul>
                    </div>

                    <!-- CONTACT -->
                    <div class="col-md-3">
                        <h5 class="mb-4 text-yellow-400 font-semibold">
                            Contact Us
                        </h5>

                        <p v-for="(address, index) in addresses" :key="index" class="text-sm mb-3 leading-6">
                            {{ address }}
                        </p>

                        <div class="space-y-3 text-sm">

                            <!-- PHONE -->
                            <div class="flex items-center gap-2">
                                <i class="bi bi-telephone-fill text-yellow-400"></i>
                                <a href="tel:+919945141393" class="text-white no-underline">
                                    +91 99451 41393
                                </a>
                            </div>

                            <!-- EMAIL -->
                            <div class="flex items-center gap-2">
                                <i class="bi bi-envelope-fill text-yellow-400"></i>
                                <a href="mailto:someshwarahospital28@gmail.com" class="text-white no-underline">
                                    someshwarahospital28@gmail.com
                                </a>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!-- BOTTOM BAR -->
        <div class="bg-yellow-400 text-blue-700 px-5 py-4">
            <div
                class="container flex flex-col md:flex-row justify-between items-center text-sm text-center md:text-left gap-2">

                <p>
                    © {{ year }} Someshwara Hospital. All rights reserved.
                </p>

                <p>
                    Powered by
                    <a href="https://quantumberg.com/" target="_blank" class="font-semibold hover:underline ">
                        Quantumberg Technologies Pvt Ltd
                    </a>
                </p>

            </div>
        </div>

    </footer>
</template>

<script setup>
import { ref, onMounted } from "vue";

/* FIXED TYPO */
setTimeout(() => { }, 1000)

const year = new Date().getFullYear()

const tagline = "Someshwara Hospital is a leading integrated super-speciality hospital dedicated to delivering high-quality, evidence-based healthcare."

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

const socialIcons = [
    { icon: "bi-instagram", url: "https://www.instagram.com/virusomashekaraiah" },
    { icon: "bi-facebook", url: "https://www.facebook.com/people/Dr-Viru-Somashekaraiah/61584730115916/" },
    { icon: "bi-youtube", url: "https://www.youtube.com/channel/UCOzcE9DQb9bRPkf6sDH_hiQ" },
    { icon: "bi-geo-alt-fill", url: "https://www.google.com/maps/place/Someshwara+Hospital/data=!4m2!3m1!1s0x0:0x9a147213dd6e2650?sa=X&ved=1t:2428&hl=en&ictx=111" },
]

const quickLinks = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about-us" },
    { name: "Our Doctors", path: "/doctors-list" },
    { name: "Blogs", path: "/blog" },
    { name: "Gallery", path: "/gallery" },
    { name: "Contact Us", path: "/contact-us" },
    { name: "Book an Appointment", path: "/appointment-page" },
]

const services = [
    { service: "Orthopedic Care" },
    { service: "Spine & Joint Disorders" },
    { service: "Regenerative Medicine" },
    { service: "Ozone Therapy Treatments" },
    { service: "Pain Management" },
    { service: "Lifestyle & Diet Management" },
]

const addresses = [
    "BH Rd, Madhavanagara, Gauribidanur, Karnataka 561208",
];
</script>