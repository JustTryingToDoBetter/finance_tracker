<template>
    <div class="min-h-screen flex flex-col items-center justify-between p-6 bg-gray-100">
      <!-- Header -->
      <header class="w-full flex justify-between">
        <h2 class="text-lg font-semibold">Finance Tracker</h2>
      </header>
  
      <!-- Main Content -->
      <main class="text-center">
        <h1 class="text-2xl font-bold">Welcome, <span class="text-blue-500">{{ username }}</span></h1>
        <p class="text-gray-600 mt-2">Ready to start tracking your finances!?</p>
  
        <!-- Savings Overview -->
        <section class="mt-6">
          <h2 class="text-xl font-semibold">Current Savings: ${{ savings }}</h2>
        </section>
  
        <!-- Navigation Menu -->
        <section class="mt-8 flex gap-6">
          <button class="px-4 py-2 bg-blue-500 text-white rounded-lg shadow-md">Goals</button>
          <button class="px-4 py-2 bg-green-500 text-white rounded-lg shadow-md">Savings</button>
          <button class="px-4 py-2 bg-red-500 text-white rounded-lg shadow-md">Expenses</button>
        </section>
      </main>
  
      <!-- Footer -->
      <footer class="text-gray-500 mt-6">
        <p>Something at the bottom</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "Username",  // Replace with dynamic data
        savings: 0,  // Replace with actual savings data
      };
    },
  };
  </script>
  