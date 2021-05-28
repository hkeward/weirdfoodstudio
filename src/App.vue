<template>
  <title-bar />
  <div id="navbar_contents">
    <div id="nav">
      <div>
        <router-link to="/about">About</router-link>
      </div>
    </div>
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>
import TitleBar from "@/components/TitleBar.vue";

export default {
  components: {
    TitleBar,
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

#nav {
  text-align: left;
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

#navbar_contents {
  display: flex;
}
</style>
