<template>
  <div id="category_gallery">
    <div
      class="gallery_column"
      v-for="column_index in num_columns"
      v-bind:key="column_index"
      v-bind:style="flexStyle"
    >
      <img
        v-for="img_obj in metadata[category].slice(
          (column_index - 1) * num_img_per_column,
          num_img_per_column * column_index
        )"
        v-bind:key="img_obj.file"
        v-bind:src="getImgUrl(img_obj)"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "CategoryGallery",
  data() {
    return {
      windowWidth: window.innerWidth,
    };
  },
  computed: {
    ...mapState(["metadata"]),
    category() {
      return this.$route.name.toLowerCase().replace(" ", "-");
    },
    num_images() {
      return this.metadata[this.category].length;
    },
    num_columns() {
      if (this.num_images <= 6) {
        return 2;
      } else {
        return 4;
      }
    },
    flexStyle() {
      var flex_basis;
      var max_width;
      if (this.windowWidth <= 990 || this.num_columns == 1) {
        flex_basis = "100%";
        max_width = "100%";
      } else if (this.windowWidth <= 1200 || this.num_columns == 2) {
        flex_basis = "50%";
        max_width = "50%";
      } else if (this.num_columns == 4) {
        flex_basis = "25%";
        max_width = "25%";
      } else {
        flex_basis = "100%";
        max_width = "100%";
      }
      return {
        flex: flex_basis,
        "max-width": max_width,
      };
    },
    num_img_per_column() {
      var num_columns = Math.ceil(this.num_images / this.num_columns);
      if (num_columns > 0) {
        return num_columns;
      } else {
        return this.num_images % this.num_columns;
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.onResize);
  },
  methods: {
    getImgUrl(img_obj) {
      return require("../assets/" + img_obj.file);
    },
    onResize() {
      this.windowWidth = window.innerWidth;
    },
  },
};
</script>

<style scoped>
#category_gallery {
  display: flex;
  flex-wrap: wrap;
}
#category_gallery img {
  width: 100%;
  margin-bottom: 5px;
  border-radius: 7px;
}
.gallery_column {
  box-sizing: border-box;
  padding: 0 20px 0 0;
}

/* TODO I broke this by putting styles directly on the items */
@media screen and (max-width: 1200px) {
  .gallery_column {
    flex: 50%;
    max-width: 50%;
  }
}

@media screen and (max-width: 990px) {
  .gallery_column {
    flex: 100%;
    max-width: 100%;
  }
}
</style>
