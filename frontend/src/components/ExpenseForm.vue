<template>
    <form @submit.prevent="submitExpense">
      <div>
        <label for="amount">Amount:</label>
        <input
          v-model="form.amount"
          type="number"
          id="amount"
          placeholder="Enter amount"
          required
          min="0"
        />
      </div>
      <div>
        <label for="category">Category:</label>
        <select v-model="form.category" id="category" required>
          <option value="">Select a category</option>
          <option>Food</option>
          <option>Transport</option>
          <option>Entertainment</option>
        </select>
      </div>
      <div>
        <label for="date">Date:</label>
        <input v-model="form.date" type="date" id="date" required />
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea v-model="form.description" id="description"></textarea>
      </div>
      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Submitting...' : 'Add Expense' }}
      </button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success">{{ successMessage }}</p>
    </form>
  </template>
  
  <script>
  import axios from "@/services/axios";
  
  export default {
    data() {
      return {
        form: { amount: '', category: '', date: '', description: '' },
        isSubmitting: false,
        errorMessage: '',
        successMessage: '',
      };
    },
    methods: {
      async submitExpense() {
        this.isSubmitting = true;
        this.errorMessage = '';
        this.successMessage = '';
  
        try {
          await axios.post("/api/expenses", this.form);
          this.successMessage = 'Expense added successfully!';
          this.resetForm();
          this.$emit("expense-added");
        } catch (error) {
          console.error("Error adding expense:", error);
          this.errorMessage = error.response?.data?.message || 'Failed to add expense. Please try again.';
        } finally {
          this.isSubmitting = false;
        }
      },
      resetForm() {
        this.form = { amount: '', category: '', date: '', description: '' };
      },
    },
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  .success {
    color: green;
  }
  </style>