<template>
  <div>
    <button @click="handleClick">Click Me</button>
  </div>
</template>

<script>
export default {
  methods: {
    handleClick() {
      this.$emit("clicked");
    },
  },
};
</script>