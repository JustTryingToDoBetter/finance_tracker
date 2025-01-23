<template>
    <div class="dashboard">
      <h1>Dashboard</h1>
      <div v-if="isLoading">Loading...</div>
      <div v-else>
        <div class="charts">
          <PieChart :data="categoryData" />
          <BarChart :data="monthlyData" />
        </div>
        <div class="summary">
          <p>Total Budget: {{ formatCurrency(budget) }}</p>
          <p>Remaining Balance: {{ formatCurrency(remaining) }}</p>
        </div>
        <div v-if="categoryData.length === 0">
          <p>No data available. Start by adding expenses!</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import PieChart from "@/components/PieChart.vue";
  import BarChart from "@/components/BarChart.vue";
  import axios from "@/services/axios";
  
  export default {
    components: { PieChart, BarChart },
    data() {
      return {
        budget: 0,
        remaining: 0,
        categoryData: [],
        monthlyData: [],
        isLoading: true,
      };
    },
    methods: {
      async fetchData() {
        this.isLoading = true;
        try {
          const budgetResponse = await axios.get("/api/budget");
          this.budget = budgetResponse.data.total_budget;
          this.remaining = budgetResponse.data.remaining_budget;
  
          const analyticsResponse = await axios.get("/api/analytics");
          this.categoryData = analyticsResponse.data.category_breakdown;
          this.monthlyData = analyticsResponse.data.monthly_totals;
        } catch (error) {
          console.error("Failed to fetch dashboard data:", error);
        } finally {
          this.isLoading = false;
        }
      },
      formatCurrency(value) {
        return new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
      },
    },
    async created() {
      await this.fetchData();
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    padding: 20px;
  }
  .charts {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
  }
  .summary {
    background: #f5f5f5;
    padding: 15px;
    border-radius: 8px;
  }
  </style>