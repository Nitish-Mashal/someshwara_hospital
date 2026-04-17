import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { getProxyOptions } from 'frappe-ui/src/utils/vite-dev-server'
import { webserver_port } from '../../../sites/common_site_config.json'

export default defineConfig({
  // ✅ Correct base path for production (important for Frappe assets)
  base: process.env.NODE_ENV === 'production'
    ? '/assets/someshwara_hospital/'
    : '/',

  plugins: [vue()],

  server: {
    port: 8081,
    proxy: getProxyOptions({ port: webserver_port }),
  },

  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },

  build: {
    // ✅ Output inside app public folder (Frappe requirement)
    outDir: `../${path.basename(path.resolve('..'))}/public/frontend`,
    emptyOutDir: true,

    // ✅ Better browser compatibility
    target: 'es2015',

    // ✅ Performance optimizations
    cssCodeSplit: true,     // faster loading
    minify: 'esbuild',      // fast + efficient minification
    sourcemap: false,       // smaller bundle size
  },

  optimizeDeps: {
    include: [
      'frappe-ui > feather-icons',
      'showdown',
      'engine.io-client',
      'debug',
    ],
    esbuildOptions: {
      target: 'esnext', // fixes async issues
    },
  },
})