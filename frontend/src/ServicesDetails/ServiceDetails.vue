<template>
    <div class="w-full mb-10">

        <!-- ================= BANNER ================= -->
        <div v-if="service" class="relative w-full mb-8 overflow-hidden">

            <img :src="serviceImage" :alt="altText" class="w-full h-[180px] sm:h-[240px] md:h-[380px] object-cover" />

            <!-- 🔵 THEME OVERLAY -->
            <div class="absolute inset-0 bg-blue-700/40"></div>

            <!-- TEXT -->
            <div class="absolute inset-0 flex items-center justify-center z-10 px-6">
                <h1 class="text-white font-semibold text-center text-2xl md:text-5xl">
                    {{ service.name1 }}
                </h1>
            </div>
        </div>

        <!-- ================= CONTENT ================= -->
        <div v-if="service" class="max-w-7xl mx-auto px-4">

            <div class="grid md:grid-cols-3 gap-8">

                <!-- LEFT CONTENT -->
                <div class="md:col-span-2">
                    <div class="text-gray-700 leading-relaxed text-[15px]" v-html="service.description">
                    </div>
                </div>

                <!-- RIGHT CONTACT FORM -->
                <div>

                    <div class="bg-white rounded-2xl shadow-lg border border-blue-100 p-6">

                        <!-- TITLE -->
                        <h5 class="text-center font-semibold text-blue-700 mb-4 text-lg">
                            Contact Us For Enquiry
                        </h5>

                        <el-form ref="contactForm" :model="form" :rules="rules" label-position="top">

                            <!-- NAME -->
                            <el-form-item label="Name" prop="name">
                                <input v-model="form.name" type="text"
                                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-700"
                                    placeholder="Enter your name" />
                            </el-form-item>

                            <!-- EMAIL -->
                            <el-form-item label="Email" prop="email">
                                <input v-model="form.email" type="email"
                                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-700"
                                    placeholder="Enter your email" />
                            </el-form-item>

                            <!-- PHONE -->
                            <el-form-item label="Phone" prop="phone">
                                <input v-model="form.phone" type="text"
                                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-700"
                                    placeholder="Enter your phone number" />
                            </el-form-item>

                            <!-- SOURCE -->
                            <el-form-item label="How did you find us?" prop="source">
                                <select v-model="form.source"
                                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-700">
                                    <option value="">Select option</option>
                                    <option value="facebook">Facebook</option>
                                    <option value="instagram">Instagram</option>
                                    <option value="google">Google</option>
                                    <option value="friend">Friend</option>
                                    <option value="other">Others</option>
                                </select>
                            </el-form-item>

                            <!-- BUTTON -->
                            <button type="button" @click="handleSubmit" :disabled="loading"
                                class="w-full mt-3 bg-yellow-400 text-white py-2 rounded-lg font-semibold hover:opacity-90 transition">
                                {{ loading ? "Sending..." : "Send Enquiry" }}
                            </button>

                            <!-- SUCCESS -->
                            <p v-if="successMsg" class="text-green-600 text-center mt-3 text-sm">
                                {{ successMsg }}
                            </p>

                            <!-- ERROR -->
                            <p v-if="errorMsg" class="text-red-500 text-center mt-3 text-sm">
                                {{ errorMsg }}
                            </p>

                        </el-form>
                    </div>

                </div>

            </div>
        </div>

        <!-- ================= LOADING ================= -->
        <div v-else class="text-center py-20 text-gray-500">
            Loading service details...
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const service = ref(null)

/* ---------------- FETCH SERVICE ---------------- */
const fetchService = async () => {
    try {
        const res = await fetch(
            "/api/method/someshwara_hospital.api.our_services.get_our_services"
        )
        const data = await res.json()

        if (data.message?.status === "success") {
            service.value = data.message.data.find(
                item => item.url === route.params.slug
            )

            updateSEO()
        }
    } catch (error) {
        console.error("Failed to fetch service details", error)
    }
}

/* ---------------- SEO META ---------------- */
const updateSEO = () => {
    if (!service.value) return

    const title =
        service.value.meta_title ||
        service.value.name1 ||
        "Someshwara Hospital"

    const description =
        service.value.meta_description ||
        "Someshwara Hospital Services"

    const keywords =
        service.value.meta_keyword ||
        "hospital, healthcare, someshwara hospital"

    document.title = title

    let metaDesc = document.querySelector('meta[name="description"]')
    if (!metaDesc) {
        metaDesc = document.createElement("meta")
        metaDesc.setAttribute("name", "description")
        document.head.appendChild(metaDesc)
    }
    metaDesc.setAttribute("content", description)

    let metaKeywords = document.querySelector('meta[name="keywords"]')
    if (!metaKeywords) {
        metaKeywords = document.createElement("meta")
        metaKeywords.setAttribute("name", "keywords")
        document.head.appendChild(metaKeywords)
    }
    metaKeywords.setAttribute("content", keywords)
}

/* ---------------- IMAGE ---------------- */
const serviceImage = computed(() => {
    if (!service.value?.thumnail_image) return ""

    return service.value.thumnail_image.startsWith("http")
        ? service.value.thumnail_image
        : service.value.thumnail_image   // ✅ FIXED
})

const altText = computed(() =>
    service.value?.name1
        ? `Someshwara Hospital - ${service.value.name1}`
        : "Someshwara Hospital"
)

/* ---------------- CONTACT FORM ---------------- */
const contactForm = ref(null)
const loading = ref(false)
const successMsg = ref("")
const errorMsg = ref("")

const form = ref({
    name: "",
    email: "",
    phone: "",
    source: "",
})

const rules = {
    name: [{ required: true, message: "Please enter your name", trigger: "blur" }],
    email: [{ required: true, message: "Please enter your email", trigger: "blur" }],
    phone: [
        { required: true, message: "Please enter Phone Number", trigger: "blur" },
        {
            validator: (rule, value, callback) => {
                const digits = value.replace(/\D/g, "")
                if (!/^[6-9]\d{9}$/.test(digits)) {
                    callback(new Error("Enter valid 10 digit mobile number"))
                } else callback()
            },
            trigger: "blur",
        },
    ],
    source: [{ required: true, message: "Please select an option", trigger: "change" }],
}

const handleSubmit = () => {
    successMsg.value = ""
    errorMsg.value = ""

    contactForm.value.validate(async (valid) => {
        if (!valid) return

        loading.value = true
        try {
            const res = await fetch(
                "/api/method/someshwara_hospital.api.contact.submit_contact", // 🔥 UPDATE THIS
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(form.value),
                }
            )

            const data = await res.json()

            if (data.message?.message === "success") {
                successMsg.value =
                    data.message.success_message ||
                    "Thank you for contacting us. We will connect shortly."
                contactForm.value.resetFields()
            } else {
                errorMsg.value = "Something went wrong. Please try again."
            }
        } catch (e) {
            errorMsg.value = "Server error. Please try later."
        } finally {
            loading.value = false
        }
    })
}

/* ---------------- WATCH ROUTE ---------------- */
watch(() => route.params.slug, () => {
    service.value = null
    fetchService()
})

/* ---------------- MOUNT ---------------- */
onMounted(fetchService)
</script>