<template>
  <div>
    <div>
      <router-link to="/">
        <div id="title_text">Weird Food Studio</div>
      </router-link>
    </div>
    <div v-if="mobile" class="nav_holder">
      <navbar :mobile="mobile" />
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  name: "TitleBar",
  props: ["mobile"],
  components: {
    Navbar,
  },
};
</script>

<style scoped>
#title_text {
  font-family: "Squada One", cursive;
  font-size: 500%;
  text-align: left;
  color: #2c3e50;
  text-decoration: none;
}

.nav_holder {
  position: fixed;
  top: 10px;
  left: 10px;
}
</style>
