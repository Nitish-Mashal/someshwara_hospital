import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/Home/Herosection.vue'),
    meta: {
      title:
        'Someshwara Hospital | Best Multispeciality Hospital in Madhavanagara, Gauribidanur',
      description:
        'Someshwara Hospital is a trusted multispeciality hospital in Madhavanagara, Gauribidanur, Karnataka offering expert healthcare, advanced treatments, experienced doctors, and compassionate patient care.',
    },
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: () => import('@/Aboutus/Aboutus.vue'),
    meta: {
      title:
        'About Us | Someshwara Hospital, Gauribidanur',
      description:
        'Learn about Someshwara Hospital in Madhavanagara, Gauribidanur, Karnataka. We are committed to providing quality healthcare services with experienced doctors and modern medical facilities.',
    },
  },
  {
    path: '/dr-virupaksha-n-s',
    name: 'Drvirupakshans',
    component: () => import('@/Aboutus/Drvirupakshans.vue'),
    meta: {
      title:
        'Dr. Virupaksha N S | Someshwara Hospital',
      description:
        'Know more about Dr. Virupaksha N S at Someshwara Hospital, Gauribidanur, Karnataka. Experienced specialist dedicated to quality patient care and advanced treatments.',
    },
  },
  {
    path: '/services',
    name: 'Services',
    component: () => import('@/ServicesDetails/Services.vue'),
    meta: {
      title:
        'Our Medical Services | Someshwara Hospital',
      description:
        'Explore the healthcare and medical services offered at Someshwara Hospital, Madhavanagara, Gauribidanur including orthopaedics, pain management, diagnostics, and speciality treatments.',
    },
  },
  {
    path: '/services/:slug',
    name: 'ServiceDetails',
    component: () => import('@/ServicesDetails/ServiceDetails.vue'),
    meta: {
      title:
        'Medical Services | Someshwara Hospital',
      description:
        'Detailed information about medical services and speciality treatments available at Someshwara Hospital, Gauribidanur, Karnataka.',
    },
  },
  {
    path: '/treatments/:slug',
    name: 'TreatmentDetails',
    component: () => import('@/TreatmentsDetails/TreatmentDetails.vue'),
    meta: {
      title:
        'Advanced Treatments | Someshwara Hospital',
      description:
        'Discover advanced treatments and expert healthcare solutions at Someshwara Hospital in Madhavanagara, Gauribidanur, Karnataka.',
    },
  },
  {
    path: '/doctors-list',
    name: 'DoctorsList',
    component: () => import('@/DoctorsList/DoctorsList.vue'),
    meta: {
      title:
        'Our Doctors | Someshwara Hospital',
      description:
        'Meet the experienced and qualified doctors at Someshwara Hospital, Gauribidanur dedicated to providing expert medical care and personalized treatments.',
    },
  },
  {
    path: '/viewProfile/:id',
    name: 'ViewProfile',
    component: () => import('@/DoctorsList/Viewprofile.vue'),
    meta: {
      title:
        'Doctor Profile | Someshwara Hospital',
      description:
        'View doctor profiles, qualifications, and specialities at Someshwara Hospital, Madhavanagara, Gauribidanur.',
    },
  },
  {
    path: '/appointment-page',
    name: 'AppointmentPage',
    component: () => import('@/Appointment/AppointmentPage.vue'),
    meta: {
      title:
        'Book Appointment | Someshwara Hospital',
      description:
        'Book an appointment with expert doctors at Someshwara Hospital, Gauribidanur, Karnataka for quality healthcare and advanced treatment services.',
    },
  },
  {
    path: '/thank-you',
    name: 'ThankYou',
    component: () => import('@/ThankYou/thankyou.vue'),
    meta: {
      title:
        'Thank You | Someshwara Hospital',
      description:
        'Thank you for contacting Someshwara Hospital. Our team will get in touch with you shortly.',
    },
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: () => import('@/Gallery/Gallery.vue'),
    meta: {
      title:
        'Hospital Gallery | Someshwara Hospital',
      description:
        'View the gallery of Someshwara Hospital, Madhavanagara, Gauribidanur showcasing our facilities, infrastructure, doctors, and patient care environment.',
    },
  },

  // ================= Blogs =================
  {
    path: '/blog',
    name: 'BlogsPreview',
    component: () => import('@/Blogs/BlogsPreview.vue'),
    meta: {
      title:
        'Health Blogs | Someshwara Hospital',
      description:
        'Read healthcare tips, medical insights, treatment guides, and wellness articles from Someshwara Hospital, Gauribidanur, Karnataka.',
    },
  },
  {
    path: '/blogdetails/:slug',
    name: 'BlogDetails',
    component: () => import('@/Blogs/BlogDetails.vue'),
    meta: {
      title:
        'Health Article | Someshwara Hospital',
      description:
        'Explore informative medical articles, treatment information, and healthcare awareness blogs by Someshwara Hospital.',
    },
  },
  {
    path: '/contact-us',
    name: 'ContactUs',
    component: () => import('@/ContactUs/Contactus.vue'),
    meta: {
      title:
        'Contact Us | Someshwara Hospital, Gauribidanur',
      description:
        'Contact Someshwara Hospital in Madhavanagara, Gauribidanur, Karnataka for appointments, enquiries, and healthcare support.',
    },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

// ================= Dynamic Meta Tags =================
router.beforeEach((to, from, next) => {
  document.title =
    to.meta.title || 'Someshwara Hospital | Gauribidanur'

  const metaDescription = document.querySelector(
    'meta[name="description"]'
  )

  if (metaDescription) {
    metaDescription.setAttribute(
      'content',
      to.meta.description ||
      'Someshwara Hospital in Madhavanagara, Gauribidanur, Karnataka provides expert healthcare services with experienced doctors and modern facilities.'
    )
  }

  next()
})

export default router