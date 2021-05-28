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
@import url("https://fonts.googleapis.com/css2?family=Squada+One&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300&display=swap");

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
