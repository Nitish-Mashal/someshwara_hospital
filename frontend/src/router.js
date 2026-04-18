import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/Home/Herosection.vue'),
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: () => import('@/Aboutus/Aboutus.vue'),
  },
  {
    path: '/dr-virupaksha-n-s',
    name: 'Drvirupakshans',
    component: () => import('@/Aboutus/Drvirupakshans.vue'),
  },
  {
    path: '/services/:slug',
    name: 'ServiceDetails',
    component: () => import('@/ServicesDetails/ServiceDetails.vue'),
    meta: {
      title: '',
      description: '',
    },
  },
  {
    path: '/doctors-list',
    name: 'DoctorsList',
    component: () => import('@/DoctorsList/DoctorsList.vue'),
    meta: {
      title: '',
      description: '',
    },
  },
  {
    path: '/viewProfile/:id',
    name: 'ViewProfile', 
    component: () => import('@/DoctorsList/Viewprofile.vue'),
  },
  {
    path: '/appointment-page',
    name: 'AppointmentPage',
    component: () => import('@/Appointment/AppointmentPage.vue'),
  },
  {
    path: '/thank-you',
    name: 'ThankYou', 
    component: () => import('@/ThankYou/thankyou.vue'),
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: () => import('@/Gallery/Gallery.vue'),
    meta: {
      title: '',
      description: '',
    },
  },

  // ================= Blogs =================
  {
    path: '/blog',
    name: 'BlogsPreview',
    component: () => import('@/Blogs/BlogsPreview.vue'),
    meta: {
      title: '',
      description:
        '',
    },
  },
  {
    path: '/blogdetails/:slug',
    name: 'BlogDetails',
    component: () => import('@/Blogs/BlogDetails.vue'),
    meta: {
      title: '',
      description:
        '',
    },
  },
  {
    path: '/contact-us',
    name: 'ContactUs',
    component: () => import('@/ContactUs/Contactus.vue'),
    meta: {
      title: '',
      description: '',
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

export default router