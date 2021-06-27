<template>
  <div class="detail">
    <div class="image">
        <img v-bind:src="getImgUrl(img_obj)" />
    </div>
    <div class="image_info">
      <strong>{{ img_obj.name }}</strong>
      <p>
        {{ img_obj.description }}
      </p>
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
  },
  methods: {
    getImgUrl(img_obj) {
      return require("../assets/" + img_obj.file);
    },
  },
  // created() {
  //     this.getCurrentArt(this.$route.params.category, this.$route.params.id)
  // }
};
</script>

<style scoped>
.detail {
  font-size: 3em;
  display: flex;
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
}
</style>
