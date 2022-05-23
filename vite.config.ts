import { defineConfig } from 'vite';
import { resolve } from 'path';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
    plugins: [vue()],
    root: resolve('./static/src'),
    base: '/static/',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        origin: 'http://localhost:3000'
    },
    resolve: {
        alias: {
            "@": resolve(__dirname, "./static/src"),
            vue: 'vue/dist/vue.esm-bundler.js',
        },
    },
    build: {
        outDir: resolve('./static/dist'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve('./static/src/main.ts'),
            },
        },
    },
});

