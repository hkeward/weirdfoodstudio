<template>
  <title-bar />
  <div id="content">
    <navbar />
    <router-view class="main_content" />
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
  mounted() {
    this.load_database();
  },
  methods: {
    ...mapActions(["load_database"]),
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

#content {
  display: flex;
}

.main_content {
  flex-basis: 70%;
}

@media screen and (max-width: 1200px) {
  .main_content {
    flex-basis: 90%;
  }
}

a {
  color: inherit;
  text-decoration: none;
}
</style>
