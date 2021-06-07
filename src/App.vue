<template>
  <title-bar />
  <div id="contents">
    <navbar />
    <router-view />
  </div>
</template>

<script>
import TitleBar from "@/components/TitleBar.vue";
import Navbar from "@/components/Navbar.vue";
import { mapActions } from "vuex";
import { mapState } from "vuex";

export default {
  components: {
    TitleBar,
    Navbar,
  },
  mounted() {
    this.load_database();
  },
  methods: {
    ...mapActions(["load_database"]),
  },
  computed: {
    ...mapState(["var1"]),
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

#contents {
  display: flex;
}

a {
  color: inherit;
  text-decoration: none;
}
</style>
