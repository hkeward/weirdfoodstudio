import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faHamburger,
  faTimesCircle,
  faArrowCircleRight,
  faArrowCircleLeft,
  faShoppingBag,
} from "@fortawesome/free-solid-svg-icons";
import {
  faInstagram,
  faEtsy,
  faPatreon,
} from "@fortawesome/free-brands-svg-icons";

library.add(
  faHamburger,
  faTimesCircle,
  faArrowCircleRight,
  faArrowCircleLeft,
  faShoppingBag,
  faInstagram,
  faEtsy,
  faPatreon
);

createApp(App)
  .use(store)
  .use(router)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
