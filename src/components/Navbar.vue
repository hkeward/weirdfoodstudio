<template>
  <div>
    <div v-if="menu_expanded" id="nav">
      <div id="nav_open_close" @click="toggle_menu" class="icon_button">
        <font-awesome-icon icon="times-circle"></font-awesome-icon>
      </div>
      <div id="links-wrapper" class="links">
        <div id="links-top" class="links">
          <router-link
            to="/collage"
            @click="scrollToTop"
            :class="{ 'is-active': subIsActive('/collage') }"
            >Collage</router-link
          >
          <router-link
            to="/fine-art"
            @click="scrollToTop"
            :class="{ 'is-active': subIsActive('/fine-art') }"
            >Fine Art</router-link
          >
          <router-link
            to="/prints"
            @click="scrollToTop"
            :class="{ 'is-active': subIsActive('/prints') }"
            >Prints</router-link
          >
          <router-link
            to="/digital"
            @click="scrollToTop"
            :class="{ 'is-active': subIsActive('/digital') }"
            >Digital</router-link
          >
          <router-link
            to="/analogue"
            @click="scrollToTop"
            :class="{ 'is-active': subIsActive('/analogue') }"
            >Analogue</router-link
          >
        </div>
        <div id="links-bottom" class="links">
          <router-link to="/about" @click="scrollToTop">About Me</router-link>
          <router-link to="/" @click="scrollToTop">Home</router-link>
        </div>
      </div>
    </div>
    <div v-else id="nav">
      <div id="nav_open_close" @click="toggle_menu" class="icon_button">
        <font-awesome-icon icon="hamburger"></font-awesome-icon>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Navbar",
  computed: {
    ...mapState(["menu_expanded"]),
  },
  methods: {
    ...mapActions(["get_set_nav_width", "toggle_menu"]),
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    subIsActive(input) {
      const paths = Array.isArray(input) ? input : [input];

      return paths.some((path) => {
        return this.$route.path.indexOf(path) === 0; // current path starts with this path string
      });
    },
  },
};
</script>

<style scoped>
#nav {
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100%;
  max-height: 100vh;
  overflow-y: auto;
  text-align: left;
  padding: 50px;
  background-color: #82ced9;
  margin-left: 20px;
  border-radius: 7px;
  font-size: 2.5em;
  color: white;
  font-weight: 900;
}

.links {
  display: flex;
  flex-direction: column;
}

#links-wrapper {
  justify-content: space-between;
  flex-basis: 90%;
}

#links-bottom {
  padding-bottom: 50px;
}

a {
  padding: 30px 0px;
}

#nav_open_close {
  text-align: center;
}

a.router-link-exact-active,
.is-active {
  color: #001d91;
}
</style>
