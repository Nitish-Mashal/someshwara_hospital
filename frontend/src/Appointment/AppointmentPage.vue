<template>
  <div>

    <!-- TOP : DEPARTMENT + DOCTOR -->
    <div class="container mx-auto px-4 mt-3">
      <div class="max-w-3xl">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <!-- Department (hidden) -->
          <div class="hidden flex flex-col">
            <label class="mb-1 font-semibold text-gray-700">Department *</label>
            <select v-model="form.department" @change="fetchDoctors"
              class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]">
              <option value="">Select Department</option>
              <option v-for="d in departments" :key="d" :value="d">
                {{ d }}
              </option>
            </select>
          </div>

          <!-- Doctor -->
          <div class="flex flex-col">
            <label class="mb-1 font-semibold text-gray-700">Doctor *</label>
            <select v-model="form.doctor" class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]">
              <option value="">Select Doctor</option>
              <option v-for="d in doctors" :key="d.name" :value="d.name">
                {{ d.full_name || d.first_name }}
              </option>
            </select>
          </div>

        </div>
      </div>
    </div>


    <!-- MAIN SECTION -->
    <section class="px-4 py-10 grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-6xl mx-auto">

      <!-- LEFT : SLOT UI -->
      <div>
        <div v-show="availableDates.length" class="bg-white rounded-xl p-4 shadow">

          <h2 class="font-bold text-xl mb-2 text-[#065f7f]">
            Select Appointment Slots
          </h2>

          <h3 class="text-lg font-semibold mb-4">
            {{ selectedDoctor?.first_name }}
          </h3>

          <!-- Date Switch -->
          <div class="flex justify-center items-center gap-4 mb-6 relative">

            <!-- Prev -->
            <button @click="prevDate" class="w-8 h-8 border rounded-full" :disabled="selectedDateIndex === 0">
              ‹
            </button>

            <!-- Date pill -->
            <div class="px-6 py-2 rounded-full bg-green-100 text-green-700 font-semibold
               flex items-center gap-2 cursor-pointer select-none" @click="openCalendar">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 7V3m8 4V3M3 11h18M5 21h14a2 2 0 002-2V7H3v12a2 2 0 002 2z" />
              </svg>

              {{ formattedDate || "Select date" }}
            </div>

            <!-- Next -->
            <button @click="nextDate" class="w-8 h-8 border rounded-full"
              :disabled="selectedDateIndex === availableDates.length - 1">
              ›
            </button>

            <!-- Hidden calendar -->
            <input ref="hiddenDateInput" type="date" class="absolute opacity-0 pointer-events-none"
              style="width:1px;height:1px" :min="minDate" @change="onCalendarSelect($event.target.value)" />
          </div>

          <!-- Slots (FIXED & SCROLL-SAFE) -->
          <div class="h-[330px] overflow-y-scroll pr-1">

            <div class="grid grid-cols-3 gap-3 min-h-full">
              <div v-if="isFetchingSlots" class="absolute inset-0 flex items-center justify-center bg-white/70 z-10">
                <div class="flex flex-col items-center gap-2">
                  <div class="w-8 h-8 border-4 border-[#065f7f] border-t-transparent rounded-full animate-spin"></div>
                  <p class="text-sm text-gray-600">Loading slots...</p>
                </div>
              </div>
              <!-- Slot buttons -->
              <button v-for="slot in availableTimes" :key="slot.id" @click="!slot.booked && selectSlot(slot)"
                :disabled="slot.booked" :class="[
                  'border rounded-lg py-2 text-sm transition w-full',
                  slot.booked
                    ? 'bg-red-500 text-white cursor-not-allowed'
                    : selectedSlot?.id === slot.id
                      ? 'bg-green-500 text-white'
                      : 'bg-white hover:bg-green-50 cursor-pointer'
                ]">
                <div>{{ formatTime(slot.display) }}</div>
                <div class="text-xs">{{ slot.custom_token_no }}</div>
              </button>

              <!-- Placeholder (keeps scroll alive) -->
              <div v-if="!isFetchingSlots && availableTimes.length === 0"
                class="col-span-3 flex items-center justify-center text-gray-400 text-sm">
                No slots available for selected date
              </div>

            </div>
          </div>

        </div>
      </div>


      <!-- RIGHT : FORM -->
      <div class="  rounded-xl shadow">
        <form @submit.prevent="submitAppointment" class="bg-white p-6 rounded-xl shadow-md space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-2">

            <!-- Name -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">Name *</label>
              <input v-model="form.name" required placeholder="Enter your name"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]" />
            </div>

            <!-- Phone -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">Phone *</label>
              <input v-model="form.phone" @input="validatePhone" maxlength="10"
                placeholder="Enter 10 digit mobile number"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]" />
              <p v-if="errors.phone" class="text-red-500 text-sm mt-1">
                {{ errors.phone }}
              </p>
            </div>
            <!-- WhatsApp Checkbox (Full Width) -->
            <div class="md:col-span-2 flex items-center gap-2 mt-1">
              <input type="checkbox" v-model="form.whatsapp_different" id="whatsapp_check"
                class="w-3 h-3 accent-[#065f7f]" />
              <label for="whatsapp_check" class="text-sm text-gray-700 cursor-pointer">
                Alternative WhatsApp number
              </label>
            </div>

            <!-- Alternative WhatsApp Number (Only if Checked) -->
            <div v-if="form.whatsapp_different" class="flex flex-col md:col-span-2">
              <label class="mb-1 font-semibold text-gray-700">
                WhatsApp Number *
              </label>
              <input v-model="form.custom_alternative_phone_number" maxlength="10"
                placeholder="Enter 10 digit WhatsApp number"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]" />
            </div>

            <!-- Age -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">Age *</label>
              <input v-model="form.age" type="number" @input="validateAge" placeholder="Enter your age"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]" />
              <p v-if="errors.age" class="text-red-500 text-sm mt-1">
                {{ errors.age }}
              </p>
            </div>

            <!-- Gender -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">Gender *</label>
              <select v-model="form.gender" class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]">
                <option value="">Select Gender</option>
                <option>Male</option>
                <option>Female</option>
              </select>
            </div>

            <!-- Appointment Type -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">
                Appointment Type *
              </label>
              <select v-model="form.appointment_type"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]">
                <option value="">Select Type</option>
                <option v-for="t in appointment_types" :key="t.name" :value="t.appointment_type">
                  {{ t.appointment_type }}
                </option>
              </select>
            </div>

            <!-- custom_email -->
            <div class="flex flex-col">
              <label class="mb-1 font-semibold text-gray-700">custom_email</label>
              <input v-model="form.custom_email" type="custom_email" placeholder="Enter your custom_email"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]" />
            </div>

            <!-- Location -->
            <div class="flex flex-col md:col-span-2 h-20">
              <label class="mb-1 font-semibold text-gray-700">Location</label>
              <textarea v-model="form.custom_location" rows="3"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]"></textarea>
            </div>

            <!-- Message -->
            <div class="flex flex-col md:col-span-2 h-20">
              <label class="mb-1 font-semibold text-gray-700">Message</label>
              <textarea v-model="form.message" rows="3"
                class="px-2 py-1 border rounded-lg focus:ring-2 focus:ring-[#065f7f]"></textarea>
            </div>

          </div>

          <!-- Submit -->
          <button type="submit" :disabled="isLoading"
            class="w-full bg-blue-700 text-white py-2 font-bold rounded-lg transition disabled:opacity-50">
            {{ isLoading ? "Submitting..." : "SUBMIT" }}
          </button>

          <!-- Errors -->
          <p v-if="slotError" class="text-red-500 text-sm mt-3 text-center">
            {{ slotError }}
          </p>
          <p v-if="apiError" class="text-red-600 text-sm mt-2 text-center">
            {{ apiError }}
          </p>
        </form>
      </div>

    </section>

    <!-- CALL CTA -->
    <div class="max-w-xl mx-auto bg-white rounded-xl shadow-md p-6 text-center mb-4">
      <p class="text-gray-900 mb-4">
        To book an appointment directly, please call the number below.
      </p>

      <a href="tel:+91-9945141393"
        class="inline-flex items-center justify-center w-full bg-blue-700 text-white font-medium py-2 rounded-lg hover:bg-blue-700 transition">
        Call +91-9945141393
      </a>
    </div>
  </div>

</template>


<script>

export default {
  name: "AppointmentPage",

  data() {
    return {
      isLoading: false,
      slotError: " ",
      apiError: "",
      departments: [],
      doctors: [],
      appointment_types: [],

      selectedDoctor: null,
      selectedSlot: null,
      isFetchingSlots: false,
      selectedDateIndex: null,
      showCalendar: false,
      // Form data
      form: {
        name: "",
        gender: "",
        custom_email: "",
        phone: "",
        age: "",
        department: "",
        doctor: "",
        date: "",
        time: "",
        custom_token_no: "",
        message: "",
        appointment_type: "",
        custom_location: "",
        whatsapp_different: false,   // checkbox
        custom_alternative_phone_number: ""
      },
      // Validation errors
      errors: {
        phone: "",
        age: "",
      },

      // Schedule
      schedule: [],
      availableDates: [],
      availableTimes: [],

      message: { text: "", type: "" },
    };
  },

  async created() {
    try {

      // ✅ Set department manually
      this.form.department = "Orthopaedics";

      const { doctor_id } = this.$route.query;

      // ✅ Load all doctors
      await this.fetchDoctors();

      // ✅ Auto select doctor if passed
      if (doctor_id) {
        this.form.doctor = doctor_id;
        this.selectedDoctor = await this.fetchDoctorById(doctor_id);
      }

    } catch (err) {
      console.error("Created hook error:", err);
    }
  },

  computed: {
    formattedDate() {
      const d = this.availableDates[this.selectedDateIndex];
      return d ? new Date(d.date).toDateString() : "Select date";
    },

    minDate() {
      return new Date().toISOString().split("T")[0];
    }
  },

  watch: {
    async "form.doctor"(doctorId) {
      if (!doctorId) return;

      this.selectedDoctor = await this.fetchDoctorById(doctorId);
      await this.fetchAppointmentTypes(doctorId);
      await this.fetchDoctorSchedule();
    }
  },

  mounted() {
    this.fetchDepartments();
    this.fetchAppointmentTypes();
  },

  methods: {
    formatTime(time) {
      if (!time) return "";

      // Handles: 09:00:00, 09:00:, 09:00
      const parts = time.split(":");
      return `${parts[0]}:${parts[1]}`; // ✅ HH:mm only
    },
    validatePhone() {
      this.form.phone = this.form.phone.replace(/\D/g, "");
      this.errors.phone =
        this.form.phone.length !== 10 ? "Enter valid 10 digit number" : "";
    },

    validateAge() {
      this.errors.age =
        !this.form.age || this.form.age <= 0 ? "Enter valid age" : "";
    },
    /* ---------------- DOCTOR DETAILS ---------------- */
    async fetchDoctorById(doctorId) {
      try {
        const res = await fetch(
          `/api/method/someshwara_hospital.api.doctor_list.get_doctor?id=${doctorId}`
        );
        const data = await res.json();
        return data.message || null;
      } catch (err) {
        console.error("Doctor fetch error:", err);
        return null;
      }
    },

    /* ---------------- APPOINTMENT TYPES ---------------- */
    async fetchAppointmentTypes(doctorId) {
      try {
        const res = await fetch(
          `/api/method/someshwara_hospital.api.Appointment_api.get_appointment_types?practitioner=${doctorId}`
        );

        const data = await res.json();

        if (data.message?.status === "success") {
          this.appointment_types = data.message.data;
        }
      } catch (err) {
        console.error("Appointment type fetch error:", err);
      }
    },

    /* ---------------- DEPARTMENTS ---------------- */
    async fetchDepartments() {
      const res = await fetch(
        "/api/method/someshwara_hospital.api.Appointment_api.get_departments"
      );
      const data = await res.json();
      if (data.message?.status === "success") {
        this.departments = data.message.data.map(d => d.department);
      }
    },

    /* ---------------- DOCTORS BY DEPARTMENT ---------------- */
    async fetchDoctors() {
      if (!this.form.department) return;

      const res = await fetch(
        `/api/method/someshwara_hospital.api.Appointment_api.get_practitioners?department=${encodeURIComponent(
          this.form.department
        )}`
      );
      const data = await res.json();
      if (data.message?.status === "success") {
        this.doctors = data.message.data;
      }
    },

    /* ---------------- DOCTOR SCHEDULE ---------------- */
    async fetchDoctorSchedule() {
      // Reset state
      this.availableDates = [];
      this.availableTimes = [];
      this.selectedDateIndex = null;
      this.schedule = [];

      if (!this.form.doctor) return;

      try {
        const res = await fetch(
          `/api/method/someshwara_hospital.api.Appointment_api.get_doctor_schedule` +
          `?practitioner=${encodeURIComponent(this.form.doctor)}`
        );

        const data = await res.json();
        if (!Array.isArray(data.message)) return;

        this.schedule = data.message;

        // Generate dates for which doctor has slots
        this.availableDates = this.generateNext3Months(this.schedule);

        // Clear slots
        this.availableTimes = [];

        // Select the first date automatically
        if (this.availableDates.length) {
          await this.selectDate(0);
        }
      } catch (err) {
        console.error("Error fetching doctor schedule:", err);
      }

    },

    generateNext3Months(schedule) {
      const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
      const dates = [];

      const startDate = new Date();
      const endDate = new Date();
      endDate.setMonth(startDate.getMonth() + 3); // +3 months

      let currentDate = new Date(startDate);

      while (currentDate <= endDate) {
        const day = days[currentDate.getDay()];

        // Include only if schedule has slots on this day
        if (schedule.some(s => s.day === day)) {
          dates.push({
            date: currentDate.toISOString().split("T")[0], // YYYY-MM-DD
            day
          });
        }

        currentDate.setDate(currentDate.getDate() + 1);
      }

      return dates;
    },
    toggleCalendar() {
      this.showCalendar = !this.showCalendar;
    },
    openCalendar() {
      const input = this.$refs.hiddenDateInput;
      if (!input) return;

      // Chrome / Edge
      if (input.showPicker) {
        input.showPicker();
      } else {
        // Safari / fallback
        input.focus();
        input.click();
      }
    },

    onCalendarSelect(date) {
      this.showCalendar = false;

      const index = this.availableDates.findIndex(d => d.date === date);

      if (index !== -1) {
        this.selectDate(index);
      } else {
        // Doctor has NO slots on this date
        this.form.date = date;
        this.availableTimes = [];
        this.selectedSlot = null;
      }
    },
    /* ---------------- DATE / SLOT SELECTION ---------------- */
    async selectDate(i) {
      // Guard checks
      if (this.isFetchingSlots) return;
      if (!this.availableDates || !this.availableDates[i]) return;

      this.isFetchingSlots = true;

      // Reset state early
      this.availableTimes = [];
      this.selectedSlot = null;

      try {
        // Set selected date
        this.selectedDateIndex = i;
        this.form.date = this.availableDates[i].date;

        const res = await fetch(
          `/api/method/someshwara_hospital.api.Appointment_api.get_doctor_schedule` +
          `?practitioner=${encodeURIComponent(this.form.doctor)}` +
          `&appointment_date=${this.form.date}`
        );

        const data = await res.json();

        // If API fails or returns no slots
        if (!data || !Array.isArray(data.message) || data.message.length === 0) {
          this.availableTimes = [];
          return;
        }

        // Remove duplicate slots
        const uniqueSlots = Array.from(
          new Map(
            data.message.map(slot => [
              `${slot.from_time}-${slot.to_time}`,
              slot
            ])
          ).values()
        );

        // Map slots for frontend
        this.availableTimes = uniqueSlots.map((s, idx) => {
          const tokenNumber = s.custom_token_no ?? idx + 1;

          return {
            id: `${tokenNumber}-${s.from_time}-${s.to_time}-${this.form.date}`,
            display: `${s.from_time} - ${s.to_time}`,
            value: s.from_time,
            custom_token_no: `${tokenNumber}`,
            booked: Boolean(s.booked)
          };
        });

      } catch (error) {
        console.error("Error fetching slots:", error);
        this.availableTimes = [];
      } finally {
        this.isFetchingSlots = false;
      }
    },


    prevDate() {
      if (this.selectedDateIndex > 0) {
        this.selectDate(this.selectedDateIndex - 1);
      }
    },

    nextDate() {
      if (this.selectedDateIndex < this.availableDates.length - 1) {
        this.selectDate(this.selectedDateIndex + 1);
      }
    },

    selectSlot(slot) {
      if (slot.booked) return;
      this.selectedSlot = slot;
      this.form.time = slot.value;
      this.form.custom_token_no = slot.custom_token_no;
      this.slotError = "";
    },

    /* ---------------- SUBMIT ---------------- */
    async submitAppointment() {

      // ---------------- SLOT VALIDATION ----------------
      if (!this.selectedSlot) {
        this.slotError = "Please select time slot";
        return;
      }

      this.slotError = "";
      this.apiError = "";
      this.isLoading = true;

      try {

        // ---------------- WHATSAPP LOGIC ----------------
        // If checkbox NOT checked → WhatsApp = phone
        // If checked → use alternative number

        let whatsappNumber = this.form.whatsapp_different
          ? this.form.custom_alternative_phone_number
          : this.form.phone;

        // Validate alternative number if checkbox checked
        if (this.form.whatsapp_different) {

          if (!this.form.custom_alternative_phone_number) {
            this.apiError = "Please enter WhatsApp number";
            this.isLoading = false;
            return;
          }

          if (this.form.custom_alternative_phone_number.length !== 10) {
            this.apiError = "Enter valid 10 digit WhatsApp number";
            this.isLoading = false;
            return;
          }
        }

        // ---------------- CREATE FORM DATA ----------------
        const formData = new FormData();

        formData.append("name1", this.form.name);
        formData.append("custom_email", this.form.custom_email);
        formData.append("gender", this.form.gender);
        formData.append("appointment_type", this.form.appointment_type);
        formData.append("appointment_date", this.form.date);
        formData.append("appointment_time", this.form.time);
        formData.append("practitioner", this.form.doctor);
        formData.append("department", this.form.department);
        formData.append("notes", this.form.message || "");
        formData.append("phone", this.form.phone);
        formData.append("age", this.form.age);

        // ✅ Token from selected slot
        formData.append("custom_token_no", this.selectedSlot.custom_token_no);

        formData.append("custom_location", this.form.custom_location);

        // ✅ NEW FIELDS FOR BACKEND
        formData.append("custom_alternative_phone_number", whatsappNumber);
        formData.append(
          "custom_whatsapp_number",
          this.form.whatsapp_different ? 1 : 0
        );

        // ---------------- API CALL ----------------
        const response = await fetch(
          "/api/method/someshwara_hospital.api.Appointment_api.create_appointment",
          {
            method: "POST",
            body: formData
          }
        );

        const data = await response.json();
        console.log("✅ API Response:", data);

        // ---------------- BACKEND ERROR ----------------
        if (data?.message?.status === "error") {
          this.apiError = data.message.message;
          return;
        }

        // ---------------- SUCCESS ----------------
        if (data?.message?.status === "success") {

          const result = data.message;

          this.resetForm();

          this.$router.push({
            path: "/thank-you",
            state: {
              appointmentId: result.appointment_id,
              appointmentDate: result.appointment_date,
              appointmentTime: result.appointment_time,
              custom_token_no: result.custom_token_no,
              practitioner_id: result.practitioner
            }
          });

          return;
        }

      } catch (error) {

        console.error("Network/API Error:", error);

        this.apiError =
          "Something went wrong. Please contact directly through given phone number.";

      } finally {

        // Always stop loading
        this.isLoading = false;

      }
    },

    resetForm() {
      this.form = {
        name: "",
        gender: "",
        custom_email: "",
        phone: "",
        department: "",
        doctor: "",
        date: "",
        time: "",
        custom_token_no: "",
        message: "",
        appointment_type: "",
      };
      this.doctors = [];
    },
  },
};
</script>
