
import { createRouter, createWebHistory } from 'vue-router';
import Auth from './components/Auth-component.vue';
import Home from './components/Home-component.vue';

const routes = [
  { path: '/auth', component: Auth },
  { path: '/home', component: Home },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
