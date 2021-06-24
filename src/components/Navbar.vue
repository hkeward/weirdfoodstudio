<template>
  <div id="nav">
    <div>
      <router-link to="/collage">Collage</router-link><br />
      <br />
      <router-link to="/fine-art">Fine Art</router-link><br />
      <br />
      <router-link to="/prints">Prints</router-link><br />
      <br />
      <router-link to="/digital">Digital</router-link><br />
      <br />
      <router-link to="/analogue">Analogue</router-link><br />
      <br />
      <br />
      <br />
      <router-link to="/about">About Me</router-link><br />
      <br />
      <router-link to="/shop">Shop</router-link>
    </div>
  </div>
</template>

<style scoped>
#nav {
  text-align: left;
  padding: 30px;
  background-color: #82ced9;
  margin-right: 60px;
  border-radius: 7px;
  font-size: 1.5em;
  color: white;
  padding-bottom: 20px;
  font-weight: 900;
}
a.router-link-exact-active {
  color: #001d91;
}
</style>
