<template>
  <div id="gallery">
    <div
      class="category_gallery"
      v-for="category in categories"
      v-bind:key="categories.indexOf(category)"
    >
      <div class="latest_image">
        <img
          v-if="metadata[category].length > 0"
          v-bind:src="getImgUrl(metadata[category][0])"
        />
      </div>
      <div class="recent_images">
        <img
          v-for="img_obj in metadata[category].slice(1, 4)"
          v-bind:key="img_obj.file"
          v-bind:src="getImgUrl(img_obj)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Gallery",
  computed: {
    ...mapState(["metadata", "categories"]),
  },
  methods: {
    getImgUrl(img_obj) {
      return require("../assets/" + img_obj.file);
    },
  },
};
</script>

<style scoped>
#gallery {
  display: flex;
  flex-direction: column;
  width: 70%;
}
img {
  object-fit: cover;
  width: 100%;
  border-radius: 7px;
}
.category_gallery {
  display: flex;
  align-items: stretch;
  margin-bottom: 10px;
}
.latest_image {
  flex-basis: 70%;
  margin-right: 5px;
}
.latest_image img {
  height: 100%;
}
.recent_images {
  flex-basis: 30%;
  display: flex;
  flex-wrap: wrap;
}
.recent_images img:first-child {
  margin-bottom: 5px;
}
.recent_images img:nth-child(2) {
  margin-bottom: 5px;
}
.recent_images img:last-child {
  margin-bottom: 0px;
}
@media screen and (max-width: 990px) {
  #gallery {
    width: 100%;
  }
  .category_gallery {
    flex-wrap: wrap;
    margin-bottom: 5px;
  }
  .latest_image {
    flex-basis: 100%;
    margin-bottom: 5px;
  }
  .recent_images {
    flex-basis: 100%;
    align-items: center;
  }
}
</style>
