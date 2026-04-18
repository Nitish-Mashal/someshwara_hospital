<template>
    <div>
        <!-- Banner -->
        <div class="relative w-full mb-6 overflow-hidden">

            <img :src="getFileUrl('contact-us-image.jpg')" alt="Someshwara Hospital Gallery"
                class="w-full h-48 sm:h-56 md:h-80 object-cover" />

            <!-- BLUE OVERLAY -->
            <div class="absolute inset-0 bg-black/30"></div>

            <!-- TEXT -->
            <div class="absolute inset-0 flex items-center justify-center px-4">
                <div class="text-center">
                    <h1 class="font-bold text-2xl md:text-4xl text-white">
                        Contact Us
                    </h1>
                </div>
            </div>
        </div>

        <!-- Main Section -->
        <div class="container py-6">
            <div class="flex justify-center items-center">

                <div
                    class="w-full max-w-7xl bg-white rounded-3xl shadow-lg overflow-hidden grid grid-cols-1 md:grid-cols-[50%_50%]">

                    <!-- LEFT: FORM -->
                    <div class="px-5 py-4 w-full">
                        <div class="md:px-5 max-w-md">

                            <h2 class="text-4xl font-bold bold-test-color mb-1">
                                Get in Touch
                            </h2>
                            <p class="text-gray-600 text-sm mb-3">
                                Have questions? We'd love to hear from you.
                            </p>

                            <!-- FORM -->
                            <el-form ref="contactForm" :model="form" :rules="rules" label-position="top">

                                <!-- Name -->
                                <el-form-item label="Name" prop="name">
                                    <input v-model="form.name" type="text" placeholder="Enter your name"
                                        class="w-full border border-gray-300 rounded-md px-3 py-1 focus:outline-none" />
                                </el-form-item>

                                <!-- Email -->
                                <el-form-item label="Email" prop="email">
                                    <input v-model="form.email" type="email" placeholder="Enter your email"
                                        class="w-full border border-gray-300 rounded-md px-3 py-1 focus:outline-none" />
                                </el-form-item>

                                <!-- Phone -->
                                <el-form-item label="Phone" prop="phone">
                                    <input v-model="form.phone" type="text" placeholder="Enter your phone number"
                                        class="w-full border border-gray-300 rounded-md px-3 py-1 focus:outline-none" />
                                </el-form-item>

                                <!-- Source -->
                                <el-form-item label="How did you find us?" prop="source">
                                    <select v-model="form.source"
                                        class="w-full border border-gray-300 rounded-md px-3 py-1 focus:outline-none">
                                        <option value="">Select option</option>
                                        <option value="facebook">Facebook</option>
                                        <option value="instagram">Instagram</option>
                                        <option value="google">Google</option>
                                        <option value="friend">Friend</option>
                                        <option value="other">Others</option>
                                    </select>
                                </el-form-item>

                                <!-- Comments -->
                                <el-form-item label="Comments">
                                    <textarea v-model="form.comments" placeholder="Enter your message"
                                        class="w-full border border-gray-300 rounded-md px-3 py-1 focus:outline-none">
                                    </textarea>
                                </el-form-item>

                                <!-- Submit -->
                                <el-button class="w-full py-2 mt-1 font-semibold rounded-md text-white transition-all"
                                    style="background-color: #1447E6;" :loading="loading" @click="handleSubmit">
                                    SEND
                                </el-button>

                                <!-- Messages -->
                                <p v-if="successMsg" class="text-green-600 mt-3 text-center text-sm">
                                    {{ successMsg }}
                                </p>

                                <p v-if="errorMsg" class="text-red-600 mt-3 text-center text-sm">
                                    {{ errorMsg }}
                                </p>

                            </el-form>
                        </div>
                    </div>

                    <!-- RIGHT SIDE -->
                    <div class="relative flex items-center bg-blue-700 p-5">
                        <div class="max-w-md mx-auto flex flex-col gap-8 text-white">

                            <!-- Contact -->
                            <div>
                                <h2 class="flex items-center gap-3 text-4xl font-bold mb-2">
                                    <span>Contact Us</span>
                                </h2>

                                <p class="mb-2">
                                    Talk to us and see how we can work this together
                                </p>

                                <p>
                                    Phone:
                                    <a href="tel:+919945141393" class="text-white">
                                        +91-9945141393
                                    </a>
                                </p>
                            </div>

                            <!-- Email -->
                            <div>
                                <h2 class="flex items-center gap-3 text-4xl font-bold mb-2">
                                    <span>Email Us</span>
                                </h2>

                                <p class="mb-2">
                                    We usually reply within 24 hours
                                </p>

                                <p>
                                    E-Mail:
                                    <a href="mailto:someshwarahospital28@gmail.com" class="text-white">
                                        someshwarahospital28@gmail.com
                                    </a>
                                </p>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!-- <AddressCards /> -->
    </div>
</template>

<script setup>
// import AddressCards from "./AddressCards.vue";
import { ref } from "vue";

const contactForm = ref(null);
const loading = ref(false);
const successMsg = ref("");
const errorMsg = ref("");

// FORM MODEL
const form = ref({
    name: "",
    email: "",
    phone: "",
    source: "",
    comments: ""
});

// VALIDATION
const rules = {
    name: [
        { required: true, message: "Please enter your name", trigger: "blur" },
    ],
    email: [
        { required: true, message: "Please enter your email", trigger: "blur" },
    ],
    phone: [
        { required: true, message: "Please enter Phone Number", trigger: "blur" },
        {
            validator: (rule, value, callback) => {
                const digitsOnly = value.replace(/\D/g, "");
                if (!digitsOnly) {
                    callback(new Error("Please enter your mobile number."));
                } else if (!/^[6-9]\d{9}$/.test(digitsOnly)) {
                    callback(new Error("Please enter valid 10 digit mobile number."));
                } else {
                    callback();
                }
            },
            trigger: "blur",
        },
    ],
    source: [
        { required: true, message: "Please select an option", trigger: "change" },
    ],
};

// SUBMIT
const handleSubmit = () => {
    successMsg.value = "";
    errorMsg.value = "";

    contactForm.value.validate(async (valid) => {
        if (!valid) return;

        loading.value = true;

        try {
            const response = await fetch(
                "/api/method/someshwara_hospital.api.contact.submit_contact",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-Requested-With": "XMLHttpRequest",
                    },
                    body: JSON.stringify({
                        name: form.value.name,
                        email: form.value.email,
                        phone: form.value.phone,
                        source: form.value.source,
                        comments: form.value.comments
                    }),
                }
            );

            const res = await response.json();

            if (res.message?.status === "success") {
                successMsg.value = res.message.message;
                contactForm.value.resetFields();
            } else {
                errorMsg.value =
                    res.message?.message || "Something went wrong. Please try again.";
            }

        } catch (err) {
            console.error(err);
            errorMsg.value = "Something went wrong. Please try again later.";
        } finally {
            loading.value = false;
        }
    });
};
</script>