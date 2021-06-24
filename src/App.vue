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
import { mapState, mapActions } from "vuex";

export default {
  components: {
    TitleBar,
    Navbar,
  },
  computed: {
    ...mapState(["nav_width"]),
    bodyMarginStyle() {
      return {
        "padding-left": this.nav_width + 80 + "px",
      };
    },
  },
  mounted() {
    this.load_database();
    this.get_set_nav_width();
  },
  methods: {
    ...mapActions(["load_database", "get_set_nav_width"]),
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
  transition: padding-left 0.5s;
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
