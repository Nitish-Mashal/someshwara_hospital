import { createRouter, createWebHistory } from 'vue-router'
const ServiceDetails = () => import('@/ServicesDetails/ServiceDetails.vue')

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
    component: ServiceDetails,
    meta: {
      title: '',
      description:
        '',
    },
  },
]

const router = createRouter({
  history: createWebHistory(), // ✅ FIXED
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

export default router