<template>
  <div>
    <div v-if="!zoomed" class="detail-wrapper">
      <div class="detail">
        <div id="image_wrapper" class="image">
          <div
            v-if="typeof prev_img_id === 'undefined'"
            class="nav_arrow_container"
          >
            <div>
              <font-awesome-icon
                icon="arrow-circle-left"
                v-bind:style="inactiveLinkStyle"
              ></font-awesome-icon>
            </div>
          </div>
          <div v-else class="icon_button nav_arrow_container">
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
          <div id="unzoomed_image">
            <img
              v-bind:src="getImgUrl(img_obj)"
              v-bind:alt="img_obj.name"
              @click="toggle_zoomed"
            />
          </div>
          <div
            v-if="typeof next_img_id === 'undefined'"
            class="nav_arrow_container"
          >
            <div>
              <font-awesome-icon
                icon="arrow-circle-right"
                v-bind:style="inactiveLinkStyle"
              ></font-awesome-icon>
            </div>
          </div>
          <div v-else class="icon_button nav_arrow_container">
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

        <div id="right_sidebar">
          <div id="info">
            <div class="image_info">
              <strong>{{ img_obj.name }}</strong>
              <p id="medium">
                {{ img_obj.medium }}
              </p>
            </div>
          </div>

          <div class="gallery_nav">
            <div>
              <router-link v-bind:to="{ path: '/' + category }">
                Back to gallery
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div id="fullpage_image" :style="zoomedImageStyle"></div>
      <div id="fullpage_nav">
        <div
          v-if="typeof prev_img_id === 'undefined'"
          class="nav_arrow_container"
        >
          <div class="nav_zoomed">
            <font-awesome-icon
              icon="arrow-circle-left"
              style="opacity: 0.3"
            ></font-awesome-icon>
          </div>
        </div>
        <router-link
          v-else
          v-bind:to="{
            name: 'Detail',
            params: { id: prev_img_id, category: category },
          }"
          @click="scrollToTop"
          class="nav_arrow_container"
        >
          <div class="icon_button nav_zoomed">
            <font-awesome-icon icon="arrow-circle-left"></font-awesome-icon>
          </div>
        </router-link>

        <div id="zoomed_spacer" @click="toggle_zoomed"></div>

        <div
          v-if="typeof next_img_id === 'undefined'"
          class="nav_arrow_container"
        >
          <div class="nav_zoomed">
            <font-awesome-icon
              icon="arrow-circle-right"
              style="opacity: 0.3"
            ></font-awesome-icon>
          </div>
        </div>
        <router-link
          v-else
          v-bind:to="{
            name: 'Detail',
            params: { id: next_img_id, category: category },
          }"
          @click="scrollToTop"
          class="nav_arrow_container"
        >
          <div class="icon_button nav_zoomed">
            <font-awesome-icon icon="arrow-circle-right"></font-awesome-icon>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "DetailView",
  props: {
    category: String,
    id: String,
    mobile: Boolean,
  },
  computed: {
    ...mapState(["id_metadata", "zoomed", "menu_expanded"]),
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
    zoomedImageStyle() {
      if (this.zoomed) {
        return {
          display: "flex",
          "background-image": 'url("' + this.getImgUrl(this.img_obj) + '")',
        };
      } else {
        return {
          display: "none",
          "background-image": "none",
        };
      }
    },
    inactiveLinkStyle() {
      if (this.mobile && this.menu_expanded) {
        return {
          opacity: 1.0,
        };
      } else {
        return {
          opacity: 0.3,
        };
      }
    },
  },
  methods: {
    ...mapActions(["toggle_zoomed"]),
    getImgUrl(img_obj) {
      return require("../assets/" + img_obj.file);
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    async handleKeyup(event) {
      if (event.keyCode === 27) {
        if (this.zoomed) {
          this.toggle_zoomed();
        }
      } else if (event.keyCode === 13) {
        this.toggle_zoomed();
      } else if (event.keyCode === 8) {
        if (this.zoomed) {
          this.toggle_zoomed();
        }
        await this.$router.push({ path: `/${this.category}` });
      } else if (event.keyCode === 37) {
        if (this.prev_img_id !== undefined) {
          await this.$router.push({
            name: "Detail",
            params: { id: this.prev_img_id, category: this.category },
          });
        }
      } else if (event.keyCode === 39) {
        if (this.next_img_id !== undefined) {
          await this.$router.push({
            name: "Detail",
            params: { id: this.next_img_id, category: this.category },
          });
        }
      }
    },
  },
  mounted() {
    window.addEventListener("keyup", this.handleKeyup);
  },
  beforeUnmount() {
    window.removeEventListener("keyup", this.handleKeyup);
  },
};
</script>

<style scoped>
#unzoomed_image {
  margin: 0 5px;
}

#image_wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

#fullpage_image,
#fullpage_nav {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100%;
}

#fullpage_image {
  background-size: contain;
  background-repeat: no-repeat no-repeat;
  background-position: center center;
  background-color: black;
}

#fullpage_nav {
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: stretch;
}

.nav_arrow_container {
  display: flex;
  height: 100%;
}

.nav_zoomed {
  margin: 15px;
  background-color: black;
  padding: 1vw;
  border-radius: 50%;
  align-self: center;
}

#zoomed_spacer {
  flex-basis: 100%;
}

.detail-wrapper {
  display: flex;
  flex-direction: column;
}

.detail_wrapper,
#image {
  flex: 100%;
}

.gallery_nav {
  display: flex;
  flex-direction: row;
  justify-content: center;
  font-size: 100%;
}

#nav_flex {
  display: flex;
  justify-content: center;
  flex-direction: row;
  padding: 1% 0;
  flex-basis: 70%;
  font-size: 120%;
}

#nav_flex_spacer {
  flex-basis: 30%;
}

.detail {
  display: flex;
  flex-basis: 100%;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: center;
  text-align: left;
  align-items: stretch;
}
img {
  border-radius: 7px;
  max-width: 100%;
}
.image {
  flex-basis: 60%;
  margin-right: 30px;
  text-align: center;
}
.image_info {
  font-size: 200%;
}

#right_sidebar {
  display: flex;
  flex-basis: 40%;
  flex-direction: column;
  align-items: stretch;
}

#info {
  background: #82ced9;
  display: flex;
  flex-direction: column;
  padding: 2%;
  border-radius: 4%;
}

#medium {
  margin-top: 2%;
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
    align-items: center;
  }
  #info {
    flex-basis: 100%;
  }
  #nav_flex {
    flex-basis: 100%;
  }
  #nav_flex_spacer {
    flex-basis: 0%;
  }
  #right_sidebar {
    flex-basis: 100%;
    padding: 0 20px;
  }
}
</style>
