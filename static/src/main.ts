import "vite/modulepreload-polyfill";
import { createApp } from "vue";
import App from "./App.vue";
import FileUpload from "@/components/FileUpload.vue";

// const app = createApp({});
const app = createApp(App);

// app.component("my-custom-component", FileUpload);

app.mount("#app");
