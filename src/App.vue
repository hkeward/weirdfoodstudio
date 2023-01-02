<template>
  <div id="main">
    <navbar v-if="windowWidth > smallScreenWidth" />
    <div id="content" v-bind:style="bodyMarginStyle">
      <title-bar
        :windowWidth="windowWidth"
        :smallScreenWidth="smallScreenWidth"
      />
      <router-view class="main_content" :windowWidth="windowWidth" />
    </div>
  </div>
</template>

<script>
import TitleBar from "@/components/TitleBar.vue";
import Navbar from "@/components/Navbar.vue";
import { mapState, mapActions } from "vuex";

export default {
  components: {
    TitleBar,
    Navbar,
  },
  data() {
    return {
      windowWidth: window.innerWidth,
      smallScreenWidth: 990,
    };
  },
  computed: {
    ...mapState(["nav_width"]),
    bodyMarginStyle() {
      return {
        "padding-left": this.nav_width + 56 + "px",
      };
    },
  },
  methods: {
    ...mapActions(["load_database", "get_set_nav_width", "toggle_menu"]),
    onResize() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= this.smallScreenWidth) {
        this.get_set_nav_width(0);
      } else {
        this.get_set_nav_width();
      }
    },
  },
  mounted() {
    this.load_database();
    this.windowWidth = window.innerWidth;
    if (this.windowWidth <= this.smallScreenWidth) {
      this.get_set_nav_width(0);
      // default to menu closed on mobile
      this.toggle_menu();
    } else {
      this.get_set_nav_width();
    }
    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.onResize);
  },
};
</script>

<style>
html {
  font-size: 100%;
}

@font-face {
  font-family: "Squada One";
  font-style: normal;
  font-weight: 400;
  src: local("Squada One"),
    url("./fonts/Squada_one_normal_400.ttf") format("truetype");
}

@font-face {
  font-family: "Titillium Web";
  font-style: normal;
  font-weight: 300;
  src: local("Titillium Web"),
    url("./fonts/Titillium_web_normal_300.ttf") format("truetype");
}

#app {
  font-family: "Titillium Web", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#main {
  display: flex;
}

#content {
  display: flex;
  flex-direction: column;
  flex-basis: 100%;
  transition: padding-left 0.5s;
}

@media screen and (max-width: 1200px) {
  #content {
    flex-basis: 100%;
  }
}

a {
  color: inherit;
  text-decoration: none;
}

.icon_button:hover {
  cursor: pointer;
}

body {
  margin: 28px;
}
</style>
