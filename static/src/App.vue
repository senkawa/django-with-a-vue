<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import HelloWorld from "@/components/HelloWorld.vue";
// TODO: upgrade to vite 3.x, will fix asset resolution https://github.com/vitejs/vite/pull/8077
import logo from "@/assets/logo.png";
</script>

<template>
    <img alt="Vue logo" :src="logo" />
    <HelloWorld msg="allo" />
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
