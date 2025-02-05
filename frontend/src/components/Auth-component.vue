<template>
    <div class="flex justify-center items-center h-screen bg-gray-100">
      <div class="bg-white p-6 rounded shadow-lg w-96">
        <h2 class="text-2xl font-semibold text-center">Sign Up / Log In</h2>
        <form @submit.prevent="handleSubmit" class="mt-4">
          <div v-if="isSignUp" class="mb-4">
            <label for="email" class="block text-gray-700">Email</label>
            <input v-model="email" type="email" id="email" class="w-full p-2 border rounded" required />
          </div>
          <div class="mb-4">
            <label for="password" class="block text-gray-700">Password</label>
            <input v-model="password" type="password" id="password" class="w-full p-2 border rounded" required />
          </div>
          <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700">
            {{ isSignUp ? "Sign Up" : "Log In" }}
          </button>
        </form>
        <p class="mt-4 text-center text-gray-600 cursor-pointer" @click="toggleForm">
          {{ isSignUp ? "Already have an account? Log In" : "Don't have an account? Sign Up" }}
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import { auth } from '../firebase.js'; // Firebase setup
  import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        isSignUp: true, // true for sign-up, false for login
      };
    },
    methods: {
      async handleSubmit() {
        try {
          if (this.isSignUp) {
            await createUserWithEmailAndPassword(auth, this.email, this.password);
            this.$router.push("/home");
          } else {
            await signInWithEmailAndPassword(auth, this.email, this.password);
            this.$router.push("/home");
          }
        } catch (error) {
          console.error("Authentication Error:", error.message);
        }
      },
      toggleForm() {
        this.isSignUp = !this.isSignUp;
      },
    },
  };
  </script>
  