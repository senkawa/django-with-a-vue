<script lang="ts">

import { defineComponent } from "vue";

export default defineComponent({
    data() {
        return {
            message: "allo"
        };
    }
});
</script>

<template>
    File: {{ message }}
</template>
