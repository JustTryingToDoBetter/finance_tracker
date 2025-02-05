<template>
    <div class="flex justify-center items-center h-screen bg-gray-100">
      <div class="bg-white p-6 rounded shadow-lg w-96">
        <h2 class="text-2xl font-semibold text-center">Welcome to Your Dashboard!</h2>
        <p class="text-center mt-4">You are now logged in.</p>
        <button @click="handleLogout" class="w-full bg-red-500 text-white py-2 rounded hover:bg-red-700 mt-4">
          Log Out
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import { auth } from '../firebase.js';
  import { signOut } from 'firebase/auth';
  
  export default {
    methods: {
      async handleLogout() {
        try {
          await signOut(auth);
          this.$router.push("/auth");
        } catch (error) {
          console.error("Error logging out:", error.message);
        }
      },
    },
  };
  </script>
  