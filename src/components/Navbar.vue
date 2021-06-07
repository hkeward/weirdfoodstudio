<template>
  <div id="nav">
    <div>
      <router-link to="/collage">Collage</router-link><br />
      <router-link to="/fine-art">Fine Art</router-link><br />
      <router-link to="/prints">Prints</router-link><br />
      <router-link to="/digital">Digital</router-link><br />
      <router-link to="/analogue">Analogue</router-link><br />
      <hr />
      <hr />
      <router-link to="/about">About</router-link><br />
      <router-link to="/shop">Shop</router-link>
    </div>
  </div>
</template>

<style scoped>
#nav {
  text-align: left;
  padding: 30px;
  background-color: #82ced9;
  margin-right: 20px;
}
a.router-link-exact-active {
  font-weight: bold;
  color: #2c3e50;
}
</style>
