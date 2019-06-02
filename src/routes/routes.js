import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Dashboard.vue";
import UserProfile from "@/pages/UserProfile.vue";
import TableList from "@/pages/TableList.vue";

/**
 * Product
 */
import ProductCreate from "@/pages/product/ProductCreate.vue";

/**
 * Login
 */
import Login from "@/pages/Auth/Login.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard
      },
      {
        path: "user",
        name: "User Profile",
        component: UserProfile
      },
      {
        path: "table",
        name: "Table List",
        component: TableList
      }
    ]
  },
  {
    path: "/product",
    component: DashboardLayout,
    redirect: "/product/create",
    children: [
      {
        path: "create",
        name: "Criar Produto",
        component: ProductCreate
      }
    ]
  },
  {
    path: "/login",
    component: Login
  }
];

export default routes;
