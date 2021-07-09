<template>
  <div class="detail-wrapper">
    <div class="detail">
      <div class="image">
        <img v-bind:src="getImgUrl(img_obj)" />
      </div>
      <div class="image_info">
        <strong>{{ img_obj.name }}</strong>
        <p>
          {{ img_obj.medium }}
        </p>
      </div>
    </div>
    <div class="gallery_nav">
      <div id="nav_flex">
        <div v-if="typeof prev_img_id === 'undefined'" class="nav_margin">
          <font-awesome-icon
            icon="arrow-circle-left"
            style="opacity: 0.3"
          ></font-awesome-icon>
        </div>
        <div v-else class="icon_button nav_margin">
          <router-link
            v-bind:to="{
              name: 'Detail',
              params: { id: prev_img_id, category: category },
            }"
            @click="scrollToTop"
          >
            <font-awesome-icon icon="arrow-circle-left"></font-awesome-icon>
          </router-link>
        </div>
        <div class="nav_margin">
          <router-link v-bind:to="{ path: '/' + category }">
            Back to gallery
          </router-link>
        </div>
        <div v-if="typeof next_img_id === 'undefined'">
          <font-awesome-icon
            icon="arrow-circle-right"
            style="opacity: 0.3"
          ></font-awesome-icon>
        </div>
        <div v-else class="icon_button">
          <router-link
            v-bind:to="{
              name: 'Detail',
              params: { id: next_img_id, category: category },
            }"
            @click="scrollToTop"
          >
            <font-awesome-icon icon="arrow-circle-right"></font-awesome-icon>
          </router-link>
        </div>
      </div>
      <div id="nav_empty"></div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "DetailView",
  props: {
    category: String,
    id: String,
  },
  computed: {
    ...mapState(["id_metadata"]),
    img_obj() {
      return this.id_metadata[this.category][this.id];
    },
    category_keys() {
      return Object.keys(this.id_metadata[this.category]);
    },
    prev_img_id() {
      var prev_id = this.category_keys[this.category_keys.indexOf(this.id) - 1];
      return prev_id;
    },
    next_img_id() {
      var next_id = this.category_keys[this.category_keys.indexOf(this.id) + 1];
      return next_id;
    },
  },
  methods: {
    getImgUrl(img_obj) {
      return require("../assets/" + img_obj.file);
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
};
</script>

<style scoped>
.detail-wrapper {
  display: flex;
  flex-direction: column;
}
.gallery_nav {
  display: flex;
  flex-direction: row;
}
#nav_flex {
  flex-basis: 70%;
  font-size: 2.5em;
  display: flex;
  justify-content: center;
  flex-direction: row;
}
#nav_empty {
  flex-basis: 30%;
}
.nav_margin {
  margin-right: 20px;
}
.detail {
  font-size: 3em;
  display: flex;
  flex-basis: 100%;
  flex-direction: row;
  flex-wrap: nowrap;
  text-align: left;
  align-items: flex-start;
}
img {
  border-radius: 7px;
  width: 100%;
}
.image {
  flex-basis: 70%;
  margin-right: 30px;
}
.image_info {
  flex-basis: 30%;
}
@media screen and (max-width: 990px) {
  .detail {
    width: 100%;
    flex-wrap: wrap;
  }
  .image {
    flex-basis: 100%;
    margin-bottom: 10px;
  }
  .image_info {
    flex-basis: 100%;
    align-items: center;
  }
  .nav_flex {
    flex-basis: 100%;
  }
}
</style>
