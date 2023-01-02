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
    path: "/contact",
    name: "Contact",
    component: About,
    meta: {
      title: "Weird Food Studio - Contact",
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
    path: "/lino",
    name: "Lino",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Lino",
    },
  },
  {
    path: "/illustrations-digital",
    name: "Illustrations-Digital",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Digital Illustrations",
    },
  },
  {
    path: "/illustrations-physical",
    name: "Illustrations-Physical",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Physical Illustrations",
    },
  },
  {
    path: "/comics",
    name: "Comics",
    component: CategoryGallery,
    meta: {
      title: "Weird Food Studio - Comics",
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
