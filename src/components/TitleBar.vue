<template>
  <div id="title_bar">
    <div id="text_display">
      <router-link to="/">
        <div id="title_text">Weird Food Studio</div>
      </router-link>
      <router-link to="/about">
        <div id="artist">Jessi Wood</div>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
#title_bar {
  font-family: "Squada One", cursive;
  display: flex;
}
#title_text {
  font-size: 6em;
  text-align: left;
  color: #2c3e50;
  text-decoration: none;
}
#artist {
  font-size: 2em;
  text-align: center;
}
</style>
