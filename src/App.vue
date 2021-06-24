<template>
  <div id="main">
    <navbar />
    <div id="content" v-bind:style="bodyMarginStyle">
      <title-bar />
      <router-view class="main_content" />
    </div>
  </div>
</template>

<script>
import TitleBar from "@/components/TitleBar.vue";
import Navbar from "@/components/Navbar.vue";
import { mapActions } from "vuex";

export default {
  components: {
    TitleBar,
    Navbar,
  },
  data() {
    return {
      navWidth: 0,
    };
  },
  computed: {
    bodyMarginStyle() {
      return {
        "padding-left": this.navWidth + 20 + "px"
      };
    },
  },
  mounted() {
    this.load_database();
    this.getWindowWidth();
    this.$nextTick(() => {
      window.addEventListener("resize", this.getWindowWidth);
    });
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.getWindowWidth);
  },
  methods: {
    ...mapActions(["load_database"]),
    getWindowWidth() {
      this.navWidth = document.getElementById("nav").clientWidth;
    },
  },
};
</script>

<style>
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
  flex-basis: 70%;
}

@media screen and (max-width: 1200px) {
  #content {
    flex-basis: 90%;
  }
}

a {
  color: inherit;
  text-decoration: none;
}
</style>
