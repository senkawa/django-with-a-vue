import { defineConfig } from 'vite';
import { resolve } from 'path';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
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
                main: resolve('./static/src/main.tsx'),
            },
        },
    },
});

