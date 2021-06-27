import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import CategoryGallery from "@/views/CategoryGallery.vue";
import DetailView from "@/views/DetailView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      title: "Weird Food Studio - Home",
    },
  },
  {
    path: "/about",
    name: "About",
    component: About,
    meta: {
      title: "Weird Food Studio - About",
    },
  },
  {
    path: "/collage",
    name: "Collage",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Collage",
    },
  },
  {
    path: "/fine-art",
    name: "Fine Art",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Fine Art",
    },
  },
  {
    path: "/prints",
    name: "Prints",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Prints",
    },
  },
  {
    path: "/digital",
    name: "Digital",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Digital",
    },
  },
  {
    path: "/analogue",
    name: "Analogue",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Analogue",
    },
  },
  {
    path: "/:category/:id",
    name: "Detail",
    component: DetailView,
    meta: {
      title: "Weird Food Studio",
    },
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.title);
  if (nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else {
    document.title = "Weird Food Studio";
  }
  next();
});

export default router;
