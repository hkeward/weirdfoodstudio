<template>
  <div id="gallery">
    <div
      class="category_gallery"
      v-for="category in categories"
      v-bind:key="categories.indexOf(category)"
    >
      <div class="latest_image">
        <router-link
          class="img_link"
          v-if="metadata[category].length > 0"
          v-bind:to="{
            name: 'Detail',
            params: { id: metadata[category][0].id, category: category },
          }"
          @click="scrollToTop"
        >
          <img v-bind:src="getImgUrl(metadata[category][0])" />
        </router-link>
      </div>
      <div class="recent_images">
        <router-link
          class="img_link"
          v-for="img_obj in metadata[category]
            .filter((img) => !img.id.includes('mock-wine-label'))
            .slice(1, 4)"
          v-bind:key="img_obj.file"
          v-bind:to="{
            name: 'Detail',
            params: { id: img_obj.id, category: category },
          }"
          @click="scrollToTop"
        >
          <img v-bind:src="getImgUrl(img_obj)" />
        </router-link>
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
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
};
</script>

<style scoped>
#gallery {
  display: flex;
  flex-direction: column;
}
img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  border-radius: 7px;
}
.img_link {
  flex-basis: 100%;
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
.recent_images a:first-child {
  margin-bottom: 5px;
}
.recent_images a:nth-child(2) {
  margin-bottom: 5px;
}
.recent_images a:last-child {
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
